from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class RIASEC_Scores(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    r_score=db.Column(db.Integer)
    i_score=db.Column(db.Integer)
    a_score=db.Column(db.Integer)
    s_score=db.Column(db.Integer)
    e_score=db.Column(db.Integer)
    c_score=db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    qualification=db.relationship('Qualification')
    subject_interests=db.relationship('Subject_interests')
    riasec_scores=db.relationship('RIASEC_Scores')

class Qualification(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    curriculum=db.Column(db.String(150))
    alevel_score=db.Column(db.String(50))
    ib_score=db.Column(db.Integer)
    polytechnic_score=db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
class Subject_interests(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    subject1=db.Column(db.String(50))
    subject2=db.Column(db.String(50))
    subject3=db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Degrees(db.Model):
    school=db.Column(db.String(150),primary_key=True)
    degree=db.Column(db.String(150),primary_key=True)
    alevel_igp=db.Column(db.String(150))
    polytechnic_igp=db.Column(db.Float)
    employability=db.Column(db.Float)
    salary=db.Column(db.Integer)
    riasec_code=db.Column(db.String(10))
    related_subject1=db.Column(db.String(50))
    related_subject2=db.Column(db.String(50))
    related_subject3=db.Column(db.String(50))
    additional_information=db.Column(db.String(500))
    a_level_prerequisite_subjects=db.Column(db.String(100))
    a_level_prerequisites=db.Column(db.String(100))

