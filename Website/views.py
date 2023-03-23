from flask import Blueprint, render_template, request, flash, jsonify, url_for,redirect
from flask_login import login_required, current_user
from .models import *
from . import db
import json
import sqlite3 as sql
import pandas as pd

conn=sql.connect('database.db')
c=conn.cursor()

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/user-info',methods=['POST','GET'])
@login_required
def add_info():
    if request.method == 'POST':
        subject1=request.form.get('subject1')
        subject2=request.form.get('subject2')
        subject3=request.form.get('subject3')
        subject_interests=Subject_interests(subject1=subject1,subject2=subject2,subject3=subject3,user_id=current_user.id)
        db.session.add(subject_interests)
        db.session.commit()
        return redirect(url_for('views.add_portfolio'))
        
    return render_template("user_info.html", user=current_user)
        
@views.route('/academic-portfolio',methods=['POST','GET'])
@login_required
def add_portfolio():
    if request.method==  'POST':
        curriculum=request.form.get('curriculum')
        if curriculum=='ALevel':
            alevel_score=request.form.get('value') #Need to put multiple fields together
            new_entry=Qualification(curriculum=curriculum,alevel_score=alevel_score,user_id=current_user.id)
        elif curriculum=='Polytechnic':
            polytechnic_score=request.form.get('Polytechnic')
            new_entry=Qualification(curriculum=curriculum,polytechnic_score=polytechnic_score,user_id=current_user.id)
        elif curriculum=='IB':
            ib_score=request.form.get('')
        db.session.add(new_entry)
        db.session.commit()

    return render_template("academic_portfolio.html", user=current_user)   
            
@views.route('/TakeTest', methods=['POST', 'GET'])
@login_required
def receive_input():
    if request.method=='POST':
        r_score,i_score,a_score,s_score,e_score,c_score=0,0,0,0,0,0
        number_of_questions=42
        for i in range(number_of_questions):
            response=request.form.get('q'+str(i))
            if response=='r':
                r_score+=1
            elif response=='i':
                i_score+=1
            elif response=='a':
                a_score+=1
            elif response=='s':
                s_score+=1
            elif response=='e':
                e_score+=1
            elif response=='c':
                c_score+=1

        riasec_scores=RIASEC_Scores(r_score=r_score,i_score=i_score,a_score=a_score,s_score=s_score,e_score=e_score,c_score=c_score,user_id=current_user.id)
        db.session.add(riasec_scores)
        db.session.commit()
        return redirect(url_for('views.add_info'))

    return render_template("take_test.html", user=current_user)

@views.route('/Recommendations',methods=['POST','GET'])
@login_required
def recommend_course():
    if request.method=='POST': 
        def max_riasec_code(riasec_code):
            riasec_array=[riasec_code.r_score,riasec_code.i_score,riasec_code.a_score,riasec_code.s_score,riasec_code.e_score,riasec_code.c_score]
            code_array=['r','i','a','s','e','c']
            top_r=[]
            print(max(riasec_array))
            for i in range(2):
                max_index=riasec_array.index(max(riasec_array))
                top_r.append(code_array[max_index])
                riasec_array.pop(max_index)
                code_array.pop(max_index)
            return top_r #Function calculates users top 2 riasec codes
        
        #Find user's riasec code and match with course riasec_codes
        riasec_code=RIASEC_Scores.query.filter_by(user_id=current_user.id).first() #riasec_code for particular user_id
        r1,r2,r3 = max_riasec_code(riasec_code)
        course_recommendations=Degrees.query.filter_by((r1 in riasec_code) or (r2 in riasec_code) or (r3 in riasec_code)).all()
        #The above line could be an error
        
        
        
        