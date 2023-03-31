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

personality_test_qns=[
    {"q": "I like to work on cars", "v": "r"},
    {"q": "I like to do puzzles", "v": "i"},
    {"q": "I am good at working independently", "v": "a"},
    {"q": "I like to work in teams", "v": "s"},
    {"q": "I am an ambitious person, I set goals for myself", "v": "e"},
    {"q": "I like to organize things (files/desks/offices)", "v": "c"},
    {"q": "I like to build things", "v": "r"},
    {"q": "I like to have clear instructions to follow", "v":"c"},
    {"q": "I like to read about art and music", "v":"a"},
    {"q": "I like to try to influence or persuade people", "v":"e"},
    {"q": "I like to do experiments", "v":"i"},
    {"q": "I like to teach or train people", "v":"s"},
    {"q": "I like trying to help people solve their problems", "v":"s"},
    {"q": "I like to take care of animals", "v":"r"},
    {"q": "I wouldn't mind working 8 hours per day in an office", "v":"c"},
    {"q": "I like selling things", "v":"e"},
    {"q": "I enjoy creative writing", "v":"a"},
    {"q": "I enjoy science", "v":"i"},
    {"q": "I am quick to take on new responsibilities", "v":"e"},
    {"q": "I am interested in healing people", "v":"s"},
    {"q": "I enjoy trying to figure out how things work", "v":"i"},
    {"q": "I like putting things together or assembling things", "v":"r"},
    {"q": "I am a creative person", "v":"a"},
    {"q": "I pay attention to details", "v":"c"},
    {"q": "I like to do filing or typing", "v":"c"},
    {"q": "I like to analyse things (problems/situations)", "v":"i"},
    {"q": "I like to play instruments or sing", "v":"a"},
    {"q": "I enjoy learning about other cultures", "v":"s"},
    {"q": "I would like to start my own business", "v":"e"},
    {"q": "I like to cook", "v":"r"},
    {"q": "I like acting in plays", "v":"a"},
    {"q": "I am a practical person", "v":"r"},
    {"q": "I like working with numebrs or charts", "v":"i"},
    {"q": "I like to get into discussions about issues", "v":"s"},
    {"q": "I am good at keeping records of my work", "v":"c"},
    {"q": "I like working outdoors","v":"r"},
    {"q": "I like to lead","v":"e"},
    {"q": "I would like to work in an office","v":"c"},
    {"q": "I'm good at math","v":"i"},
    {"q": "I like helping people","v":"s"},
    {"q": "I like to draw","v":"a"},
    {"q": "I like to give speeches","v":"e"}
    ]
#42 questions in total

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html", user=current_user)



@views.route('/TakeTest1', methods=['POST', 'GET'])
@login_required
def personality_test1():
    if request.method=='POST':
        users_scores=RIASEC_Scores.query.filter_by(user_id=current_user.id).first()
        r_score,i_score,a_score,s_score,e_score,c_score=0,0,0,0,0,0
        total_questions=42
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
                                        s_score=s_score,e_score=e_score,c_score=c_score,
                                        completed=False,user_id=current_user.id)
        #adds a new instance regardless if user has taken the quiz or not
        
        db.session.add(riasec_scores)
        db.session.commit()
        

        return redirect(url_for('views.add_info'))

    return render_template("take_test1.html", user=current_user, pt_qns=personality_test_qns)


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
        
        descriptions=Holland_Codes.query.filter_by(id=1).first()
        print(getattr(descriptions,r1))
        print(getattr(descriptions,r2))
        print(getattr(descriptions,r3))
        

        subject_interests=Subject_interests.query.filter_by(user_id=current_user.id).first()

        by_college,general_course_list=sortRiasecAndSubject(r1,r2,r3,subject_interests.subject1,subject_interests.subject2,subject_interests.subject3)
        by_college=sortCoursesByCollege(by_college)
        general_course_list=sortCoursesGenerally(general_course_list)
        
        
        course_reco=users_courses.query.filter_by(user_id=current_user.id).first()
        if course_reco==None: 
            course_reco=users_courses(by_school_data=by_college,
                                    general_data=general_course_list,
                                    user_id=current_user.id)
            db.session.add(course_reco)
        else:
            course_reco.by_school_data=by_college
            course_reco.general_data=general_course_list
        db.session.commit()
    
        return redirect(url_for('views.view_results'))
    

    return render_template("academic_portfolio.html", user=current_user)   
            

@views.route('/view_results',methods=['POST','GET'])
@login_required
def view_results():
    
    course_reco=users_courses.query.filter_by(user_id=current_user.id).all() #should only return 1
    
    for schools in course_reco.by_school_data:
        for i in range(3):
            print(course_reco.by_school_data[schools][i])
    
    
    return render_template("view_results.html", user=current_user,
                           by_school=course_reco.by_school_data,
                           general_data=course_reco.general_data)



