from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import *
from . import db
import json
import sqlite3 as sql

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
        
        curriculum=request.form.get('curriculum')
        if curriculum=='ALevel':
            alevel_score=request.form.get('ALevel') #Need to put multiple fields together
            new_entry=Qualification(curriculum=curriculum,alevel_score=alevel_score,user_id=current_user.id)
        elif curriculum=='Polytechnic':
            polytechnic_score=request.form.get('Polytechnic')
            new_entry=Qualification(curriculum=curriculum,polytechnic_score=polytechnic_score,user_id=current_user.id)
        db.session.add(new_entry)
        db.session.commit()
        
    return render_template("user_info.html", user=current_user)
            
        
            
            
        

