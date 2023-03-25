from flask import Blueprint, render_template, request, flash, jsonify, url_for,redirect
from flask_login import login_required, current_user
from .models import *
from . import db
from sqlalchemy import or_
import json
import sqlite3 as sql
import pandas as pd
import time
from itertools import chain
from collections import defaultdict

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

@views.route('/TakeTest1', methods=['POST', 'GET'])
@login_required
def personality_test1():
    if request.method=='POST':
        r_score,i_score,a_score,s_score,e_score,c_score=0,0,0,0,0,0
        total_questions=7
        for i in range(total_questions):
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
                
        riasec_scores=RIASEC_Scores(r_score=r_score,i_score=i_score,a_score=a_score,
                                    s_score=s_score,e_score=e_score,c_score=c_score,user_id=current_user.id)
        db.session.add(riasec_scores)
        db.session.commit()
        return redirect(url_for('views.personality_test2'))

    return render_template("take_test1.html", user=current_user)

@views.route('/TakeTest2', methods=['POST', 'GET'])
@login_required
def personality_test2():
    if request.method=='POST':
        r_score,i_score,a_score,s_score,e_score,c_score=0,0,0,0,0,0
        total_questions=7
        users_scores=RIASEC_Scores.query.filter_by(user_id=current_user.id).first()
        for i in range(total_questions):
            response=request.form.get('q'+str(i))
            if response=='r':
                users_scores.r_score+=1
            elif response=='i':
                users_scores.i_score+=1
            elif response=='a':
                users_scores.a_score+=1
            elif response=='s':
                users_scores.s_score+=1
            elif response=='e':
                users_scores.e_score+=1
            elif response=='c':
                users_scores.c_score+=1
        
        db.session.commit()
        # riasec_scores=RIASEC_Scores(r_score=r_score,i_score=i_score,a_score=a_score,
        #                             s_score=s_score,e_score=e_score,c_score=c_score,user_id=current_user.id)
        # db.session.add(riasec_scores)
        # db.session.commit()
        return redirect(url_for('views.personality_test3'))

    return render_template("take_test2.html", user=current_user)

@views.route('/TakeTest3', methods=['POST', 'GET'])
@login_required
def personality_test3():
    if request.method=='POST':
        r_score,i_score,a_score,s_score,e_score,c_score=0,0,0,0,0,0
        total_questions=7
        users_scores=RIASEC_Scores.query.filter_by(user_id=current_user.id).first()
        for i in range(total_questions):
            response=request.form.get('q'+str(i))
            if response=='r':
                users_scores.r_score+=1
            elif response=='i':
                users_scores.i_score+=1
            elif response=='a':
                users_scores.a_score+=1
            elif response=='s':
                users_scores.s_score+=1
            elif response=='e':
                users_scores.e_score+=1
            elif response=='c':
                users_scores.c_score+=1
        
        db.session.commit()
        # riasec_scores=RIASEC_Scores(r_score=r_score,i_score=i_score,a_score=a_score,
        #                             s_score=s_score,e_score=e_score,c_score=c_score,user_id=current_user.id)
        # db.session.add(riasec_scores)
        # db.session.commit()
        return redirect(url_for('views.personality_test4'))

    return render_template("take_test3.html", user=current_user)

@views.route('/TakeTest4', methods=['POST', 'GET'])
@login_required
def personality_test4():
    if request.method=='POST':
        r_score,i_score,a_score,s_score,e_score,c_score=0,0,0,0,0,0
        total_questions=7
        users_scores=RIASEC_Scores.query.filter_by(user_id=current_user.id).first()
        for i in range(total_questions):
            response=request.form.get('q'+str(i))
            if response=='r':
                users_scores.r_score+=1
            elif response=='i':
                users_scores.i_score+=1
            elif response=='a':
                users_scores.a_score+=1
            elif response=='s':
                users_scores.s_score+=1
            elif response=='e':
                users_scores.e_score+=1
            elif response=='c':
                users_scores.c_score+=1
        
        db.session.commit()
        # riasec_scores=RIASEC_Scores(r_score=r_score,i_score=i_score,a_score=a_score,
        #                             s_score=s_score,e_score=e_score,c_score=c_score,user_id=current_user.id)
        # db.session.add(riasec_scores)
        # db.session.commit()
        return redirect(url_for('views.personality_test5'))

    return render_template("take_test4.html", user=current_user)

@views.route('/TakeTest5', methods=['POST', 'GET'])
@login_required
def personality_test5():
    if request.method=='POST':
        r_score,i_score,a_score,s_score,e_score,c_score=0,0,0,0,0,0
        total_questions=7
        users_scores=RIASEC_Scores.query.filter_by(user_id=current_user.id).first()
        for i in range(total_questions):
            response=request.form.get('q'+str(i))
            if response=='r':
                users_scores.r_score+=1
            elif response=='i':
                users_scores.i_score+=1
            elif response=='a':
                users_scores.a_score+=1
            elif response=='s':
                users_scores.s_score+=1
            elif response=='e':
                users_scores.e_score+=1
            elif response=='c':
                users_scores.c_score+=1
        
        db.session.commit()
        # riasec_scores=RIASEC_Scores(r_score=r_score,i_score=i_score,a_score=a_score,
        #                             s_score=s_score,e_score=e_score,c_score=c_score,user_id=current_user.id)
        # db.session.add(riasec_scores)
        # db.session.commit()
        return redirect(url_for('views.personality_test6'))

    return render_template("take_test5.html", user=current_user)

@views.route('/TakeTest6', methods=['POST', 'GET'])
@login_required
def personality_test6():
    if request.method=='POST':
        r_score,i_score,a_score,s_score,e_score,c_score=0,0,0,0,0,0
        total_questions=7
        users_scores=RIASEC_Scores.query.filter_by(user_id=current_user.id).first()
        for i in range(total_questions):
            response=request.form.get('q'+str(i))
            if response=='r':
                users_scores.r_score+=1
            elif response=='i':
                users_scores.i_score+=1
            elif response=='a':
                users_scores.a_score+=1
            elif response=='s':
                users_scores.s_score+=1
            elif response=='e':
                users_scores.e_score+=1
            elif response=='c':
                users_scores.c_score+=1
        
        db.session.commit()
        # riasec_scores=RIASEC_Scores(r_score=r_score,i_score=i_score,a_score=a_score,
        #                             s_score=s_score,e_score=e_score,c_score=c_score,user_id=current_user.id)
        # db.session.add(riasec_scores)
        # db.session.commit()
        return redirect(url_for('views.add_info'))

    return render_template("take_test6.html", user=current_user)

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
        return redirect(url_for('views.recommend_course'))

    return render_template("academic_portfolio.html", user=current_user)   
            

@views.route('/Recommendations',methods=['POST','GET'])
@login_required
def recommend_course():
    if request.method=='POST': 
        def max_riasec_code(riasec_code):
            riasec_array=[riasec_code.r_score,riasec_code.i_score,riasec_code.a_score,riasec_code.s_score,riasec_code.e_score,riasec_code.c_score]
            code_array=['r','i','a','s','e','c']
            top_r=[]
            print(max(riasec_array))
            for i in range(3):
                max_index=riasec_array.index(max(riasec_array))
                top_r.append(code_array[max_index])
                riasec_array.pop(max_index)
                code_array.pop(max_index)
            return top_r #Top 3 riasec codes are returned
        
        def sortRiasecAndSubject(r1,r2,r3,s1,s2,s3):
            # dict1 = {"Medicine":[{"school_name": "NUS", "matches_riasec": 1, "matches_subject":2}, {"school_name": "NTU", "matches_riasec": 3, "matches_subject":4}]}
            # dict1["Medicine"] -> [{"school_name": "NUS", "matches_riasec": 1, "matches_subject":2}, {"school_name": "NTU", "matches_riasec": 3, "matches_subject":4}]
            # dict1["Medicine"][1] -> {"school_name": "NTU", "matches_riasec": 3, "matches_subject":4}
            # dict1["Medicine"][1]["school_name"] -> NTU
            
            by_course=defaultdict(list) # nested dict
            by_college=defaultdict(list)
            # recommend1=defaultdict(list)
            # recommend2=defaultdict(list)

            total_score=0
            riasec_user=r1+r2+r3 #Concatenate riasec code
            # data -> [('i', 'Medicine', 'NTU', 'chemistry', 'biology', 'physics'), ('i', 'Medicine', 'NUS', 'chemistry', 'biology', 'physics')]]
            data = Degrees.query.with_entities(Degrees.riasec_code, Degrees.degree, 
                                               Degrees.school, Degrees.related_subject1, 
                                               Degrees.related_subject2, Degrees.related_subject3,
                                               Degrees.alevel_igp,Degrees.polytechnic_igp).all()

            H2_RP={'A':20,'B':17.5,'C':15,'D':12.5,'E':10,'S':5,'U':0} #H2 Rank Points
            H1_RP={'A':10,'B':8.75,'C':7.5,'D':6.25,'E':5,'S':2.5,'U':0} #H1 Rank Points
            
            user=User.query.filter_by(user_id=current_user.id).first()
            if user.qualification.curriculum == "ALevel":
                user_score=user.qualification.alevel_score
                rank_point=0
                rank_point+=H2_RP[user_score[0]]
                rank_point+=H2_RP[user_score[1]]
                rank_point+=H2_RP[user_score[2]]
                rank_point+=H1_RP[user_score[3]]
                
            for i in range(len(data)): # data[0] -> ('i', 'Medicine', 'NTU', 'chemistry', 'biology', 'physics')
                riasec_code = data[i][0]
                degree = data[i][1]
                school = data[i][2]
                related_subject1 = data[i][3]
                related_subject2 = data[i][4]
                related_subject3 = data[i][5]
                alevel_IGP=data[i][6]
                polytechnic_IGP=data[i][7]
                
                if user.qualification.curriculum=="ALevel":
                    degree_rank_point=0
                    degree_rank_point+=H2_RP[user_score[0]]
                    degree_rank_point+=H2_RP[user_score[1]]
                    degree_rank_point+=H2_RP[user_score[2]]
                    degree_rank_point+=H1_RP[user_score[3]]
                    if degree_rank_point>rank_point:
                        continue
                elif user.qualification.polytechnic_score<polytechnic_IGP:
                    continue
                
                curr_dict = {}
                curr_dict["school_name"] = school
                curr_dict["degree"]=degree
                match_str=""

                riasec_points=0
                for i,letter in enumerate(riasec_user): 
                    if letter in riasec_code: #if there exists a match between user and course riasec code
                        riasec_points+=3-i
                        match_str+=letter #r1>r2>r3
            
                #r1,r2,r3 -> 7 
                #r1,r2 -> 5
                #r1,r3 -> 4
                #r2,r3 -> 3
                #r1 -> 3
                #r2 -> 2
                #r3 -> 1 
            
                curr_dict["riasec_matches"]=match_str
                #matches_riasec=len(match_str) 
                #curr_dict["matches_riasec"] = matches_riasec

                subject_points=0
                if s1==related_subject1 or s1==related_subject2 or s1==related_subject3:
                   subject_points+=3
                if s2==related_subject1 or s2==related_subject2 or s2==related_subject3:
                    subject_points+=2
                if s3==related_subject1 or s3==related_subject2 or s3==related_subject3:
                    subject_points+=1
                
            
                curr_dict["total_score"] = riasec_points*subject_points 
                # if total_score==9:
                #     recommend1[degree].append(curr_dict)
                # if total_score==6:
                #     recommend2[degree].append(curr_dict)
            
                # curr_dict -> {"school_name": NTU,"Degree":"Mathematics", "matches_riasec": "ric", "total_score":42 }

                by_course[degree].append(curr_dict)
                by_college[school].append(curr_dict)
                return by_course,by_college
                # dict1 -> {"Mathematics": [{"school_name": NTU,"Degree":"Mathematics", "matches_riasec": "ric", "total_score":42 }]}
            #print(recommend1,recommend2,flush=True)    
        
        riasec_code=RIASEC_Scores.query.filter_by(user_id=current_user.id).first() #riasec_code for particular user_id 
        subject_interests=Subject_interests.query.filter_by(user_id=current_user.id).first()
        s1=subject_interests.subject1
        s2=subject_interests.subject2
        s3=subject_interests.subject3

        print(s1,s2,s3,flush=True)
        r1,r2,r3= max_riasec_code(riasec_code) #r1>r2>r3
        print(r1,r2,r3,flush=True)

 
        

        sortRiasecAndSubject(r1,r2,r3,s1,s2,s3)
        
        # for key in finaldict:
            
        #     def compare(item1, item2):
        #     if fitness(item1) < fitness(item2):
        #         return -1
        #     elif fitness(item1) > fitness(item2):
        #         return 1
        #     else:
        #         return 0

        # Calling
        # list.sort(key=compare)


        # filter_by_riasec_code=Degrees.query.filter(or_(Degrees.riasec_code.like(f'%{r1}%'), Degrees.riasec_code.like(f'%{r2}%'))).all()
        # filter_by_riasec_code=Degrees.query.filter((Degrees.riasec_code.like(f'%{r1}%'))).all() # TEST
        # print(filter_by_riasec_code,flush=True)
        # for degree in filter_by_riasec_code:
        #     print(degree.degree, flush=True)
        
    return render_template("recommendations.html", user=current_user)
        
        
        
        