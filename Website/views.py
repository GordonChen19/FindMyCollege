from flask import Blueprint, render_template, request, flash, jsonify, url_for,redirect,session
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
        users_scores=RIASEC_Scores.query.filter_by(user_id=current_user.id).first()
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
        if(users_scores==None):
            riasec_scores=RIASEC_Scores(r_score=r_score,i_score=i_score,a_score=a_score,
                                        s_score=s_score,e_score=e_score,c_score=c_score,user_id=current_user.id)
            db.session.add(riasec_scores)
            db.session.commit()
        else:
            users_scores.r_score=r_score
            users_scores.i_score=i_score
            users_scores.a_score=a_score
            users_scores.s_score=s_score
            users_scores.e_score=e_score
            users_scores.c_score=c_score
            db.session.commit()
        return redirect(url_for('views.personality_test2'))

    return render_template("take_test1.html", user=current_user)

@views.route('/TakeTest2', methods=['POST', 'GET'])
@login_required
def personality_test2():
    if request.method=='POST':
        question_set=2
        users_scores=RIASEC_Scores.query.filter_by(user_id=current_user.id).first()
        for i in range((question_set-1)*7,question_set*7):
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
        question_set=3
        users_scores=RIASEC_Scores.query.filter_by(user_id=current_user.id).first()
        for i in range((question_set-1)*7,question_set*7):
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
        question_set=4
        users_scores=RIASEC_Scores.query.filter_by(user_id=current_user.id).first()
        for i in range((question_set-1)*7,question_set*7):
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
        question_set=5
        users_scores=RIASEC_Scores.query.filter_by(user_id=current_user.id).first()
        for i in range((question_set-1)*7,question_set*7):
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
        question_set=6
        users_scores=RIASEC_Scores.query.filter_by(user_id=current_user.id).first()
        for i in range((question_set-1)*7,question_set*7):
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
        users_subject_interests=Subject_interests.query.filter_by(user_id=current_user.id).first()
        subject1=request.form.get('subject1')
        subject2=request.form.get('subject2')
        subject3=request.form.get('subject3')  
        if users_subject_interests==None:
            subject_interests=Subject_interests(subject1=subject1,subject2=subject2,subject3=subject3,user_id=current_user.id)
            db.session.add(subject_interests)
        else:
            users_subject_interests.subject1=subject1
            users_subject_interests.subject2=subject2
            users_subject_interests.subject3=subject3
        db.session.commit()
        return redirect(url_for('views.add_portfolio'))
        
    return render_template("user_info.html", user=current_user)
        
@views.route('/academic-portfolio',methods=['POST','GET'])
@login_required
def add_portfolio():
    if request.method==  'POST':
        users_qualification= Qualification.query.filter_by(user_id=current_user.id).first()
        curriculum=request.form.get('curriculum')
        if curriculum=='ALevel':
            alevel_score=request.form.get('alevel_score') #Need to put multiple fields together
            if users_qualification==None:
                new_entry=Qualification(curriculum=curriculum,alevel_score=alevel_score,user_id=current_user.id)
                db.session.add(new_entry)
            else:
                users_qualification.curriculum=curriculum
                users_qualification.alevel_score=alevel_score
                users_qualification.polytechnic_score=None
        elif curriculum=='Polytechnic':
            polytechnic_score=request.form.get('polytechnic_score')
            if users_qualification==None:
                new_entry=Qualification(curriculum=curriculum,polytechnic_score=polytechnic_score,user_id=current_user.id)
                db.session.add(new_entry)
            else:
                users_qualification.curriculum=curriculum
                users_qualification.polytechnic_score=polytechnic_score
                users_qualification.alevel_score=None
        elif curriculum=='IB':
            ib_score=request.form.get('')
        
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
            by_college=defaultdict(list)
            general_course_list=[]
            
            riasec_user=r1+r2+r3 #Concatenate riasec code
            # data -> [('i', 'Medicine', 'NTU', 'chemistry', 'biology', 'physics'), ('i', 'Medicine', 'NUS', 'chemistry', 'biology', 'physics')]]
            
            data = Degrees.query.all()

            H2_RP={'A':20,'B':17.5,'C':15,'D':12.5,'E':10,'S':5,'U':0} #H2 Rank Points
            H1_RP={'A':10,'B':8.75,'C':7.5,'D':6.25,'E':5,'S':2.5,'U':0} #H1 Rank Points
            
            user_qualification=Qualification.query.filter_by(id=current_user.id).first()
                
            if user_qualification.curriculum == "ALevel":
                user_score=user_qualification.alevel_score
                rank_point=0
                rank_point+=H2_RP[user_score[0]]
                rank_point+=H2_RP[user_score[1]]
                rank_point+=H2_RP[user_score[2]]
                rank_point+=H1_RP[user_score[3]]
                
            for course in data: # data[0] -> ('i', 'Medicine', 'NTU', 'chemistry', 'biology', 'physics','AAAB','-')
                riasec_code = course.riasec_code
                degree = course.degree
                school = course.school
                related_subject1 = course.related_subject1
                related_subject2 = course.related_subject2
                related_subject3 = course.related_subject3
                alevel_IGP=course.alevel_igp
                polytechnic_IGP=course.polytechnic_igp
                
                if user_qualification.curriculum=="ALevel":
                    degree_rank_point=0
                    if alevel_IGP!=None:
                        degree_rank_point+=H2_RP[alevel_IGP[0]]
                        degree_rank_point+=H2_RP[alevel_IGP[1]]
                        degree_rank_point+=H2_RP[alevel_IGP[2]]
                        degree_rank_point+=H1_RP[alevel_IGP[3]]
                        if degree_rank_point>rank_point:
                            continue #skip degree if doesnt meet requirements
                elif user_qualification.curriculum=="Polytechnic":
                    if user_qualification.polytechnic_score!=None and user_qualification.polytechnic_score<polytechnic_IGP:
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

                subject_points=0
                if s1==related_subject1 or s1==related_subject2 or s1==related_subject3:
                   subject_points+=3
                if s2==related_subject1 or s2==related_subject2 or s2==related_subject3:
                    subject_points+=2
                if s3==related_subject1 or s3==related_subject2 or s3==related_subject3:
                    subject_points+=1
                


                by_college[school].append((school,degree,match_str,riasec_points*subject_points)) 
                general_course_list.append((school,degree,match_str,riasec_points*subject_points))
            return by_college,general_course_list
        # dict1 -> {"NTU": [["school_name","Degree", "matches_riasec", total_score],["school_name","Degree", "matches_riasec", "total_score"]]}     
        def sortCoursesByCollege(by_college):
            for schools in by_college: #iterate through the schools
                by_college[schools].sort(key=lambda x:x[3],reverse=True)
            return by_college
        
        def sortCoursesGenerally(general_course_list):
            general_course_list.sort(key=lambda x:x[3],reverse=True)
            return general_course_list
            
        riasec_code=RIASEC_Scores.query.filter_by(user_id=current_user.id).first() #riasec_code for particular user_id 
        r1,r2,r3= max_riasec_code(riasec_code) #r1>r2>r3
        subject_interests=Subject_interests.query.filter_by(user_id=current_user.id).first()

        by_college,general_course_list=sortRiasecAndSubject(r1,r2,r3,subject_interests.subject1,subject_interests.subject2,subject_interests.subject3)
        by_college=sortCoursesByCollege(by_college)
        general_course_list=sortCoursesGenerally(general_course_list)
        
        print("sorted recommended courses")
        
        # for schools in by_college:
        #     for i in range(3):
        #         print(by_college[schools][i])


        return redirect(url_for('views.recommend_course'))
        
    return render_template("recommendations.html", user=current_user)


#session['degree']=degree
#return redirect(url_for('course_information'))
@views.route('/CourseInformation',methods=['POST','GET'])
def course_information():
    degree=session.get('degree',None)
    print("printing course information")
    print(degree.school)
    print(degree.degree)
    print(degree.employability)
    print(degree.salary)
    
        
    return render_template("recommendations.html", user=current_user)