from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User 
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 
from flask_login import login_user, login_required, logout_user, current_user

# Login page

auth = Blueprint('auth',__name__) 

@auth.route('/login', methods=['GET','POST']) 
def login():  

    if request.method == 'POST': 
        email = request.form.get('email') 
        password = request.form.get('password') 

        user = User.query.filter_by(email=email).first() 
        if user: 
            if check_password_hash(user.password, password): 
                flash('Logged in successfully!', 'message') 
                login_user(user, remember=True) 
                return redirect(url_for('views.home'))
            else: 
                flash('Incorrect password', 'error') 
        else: 
            flash('Email does not exist', 'error') 

    return render_template("login.html")   


@auth.route('/logout') 
@login_required 
def logout():  
    logout_user() 
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET','POST']) 
def sign_up(): 
    
    if request.method == 'POST': 
        email = request.form.get('email') 
        firstName = request.form.get('firstName')  
        lastName = request.form.get('lastName')  
        password = request.form.get('password')  
        confirm_password = request.form.get('confirm-password')  

        user = User.query.filter_by(email=email).first() 

        if user: 
            flash('Email already exists', 'error') 
        elif len(email) < 4: 
            flash('Your email is too short!', category='error')
        elif password != confirm_password: 
            flash('Confirmed password doesn\'t match!', category='error')  
        elif len(password) < 2: 
            flash('Length of password must be more than 2!', category='error')  
        else: 
            # add user to database 
            new_user = User(email=email, first_name=firstName, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user) 
            db.session.commit() 
            flash('Account successfully created!', category='message')  
            login_user(user, remember=True) 
            return redirect(url_for('views.home')) 

    return render_template("sign_up.html") 