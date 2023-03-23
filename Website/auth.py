from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User,Degrees
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
import pandas as pd

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                Degrees.query.delete()
                df=pd.read_csv('Website/static/Degree.csv') #Load Degree dataset into database
                for _, row in df.iterrows():
                    degree = Degrees(school=row['School'], degree=row['Degree'],alevel_igp=row['A_Level_IGP'],polytechnic_igp=row['Poly_IGP'],employability=row['Percentage_Of_Employed_Graduates'],salary=row['Mean_Gross_Monthly_Salary'],riasec_code=row['riasec_code'])
                    db.session.add(degree)
                    db.session.commit()
                print("Done loading")
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            Degrees.query.delete()
            df=pd.read_csv('Website/static/Degree.csv') #Load Degree dataset into database
            for _, row in df.iterrows():
                degree = Degrees(school=row['School'], degree=row['Degree'],alevel_igp=row['A_Level_IGP'],polytechnic_igp=row['Poly_IGP'],employability=row['Percentage_Of_Employed_Graduates'],salary=row['Mean_Gross_Monthly_Salary'],riasec_code=row['riasec_code'])
                db.session.add(degree)
                db.session.commit()

            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)