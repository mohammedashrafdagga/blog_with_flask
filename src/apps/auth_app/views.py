from flask import ( 
                   Blueprint, render_template, request, redirect, session, url_for,
                   flash)

from .models import User
from database import db_session



# user app
auth_app = Blueprint('user', __name__, url_prefix = '/auth')


# Login_page Method 
@auth_app.route('/login',  methods=["GET", "POST"])
def login_page():
    '''
        login user into system
    '''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email = email).first()
        
        if user is None:
            flash('user is not founded', 'error')
            return redirect(url_for('user.login_page'))
        elif not user.check_password(password):
            flash('Invalid email or password', 'error')
            return redirect(url_for('user.login_page'))
        else: 
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('articles.homepage'))
    
    return render_template('pages/login.html')
    
    
    
@auth_app.route('register', methods=["GET", "POST"])
def register_page():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
   
        # Verify that the email address is not already in use
        existing_user = User.query.filter_by(email=email, username = username).first()
        if existing_user is not None:
            flash('Email address is already in use', 'error')
            return redirect(url_for('user.register_page'))

        name = request.form['name']
        password = request.form['password']
        password1 = request.form['confirm-password']
        # Create a new user object and add it to the database
        if password != password1:
            flash('Email address is already in use', 'error')
            return redirect(url_for('user.register_page'))
        
        new_user = User(email=email,username = username, name = name,  password=password)
        db_session.add(new_user)
        db_session.commit()

        # Log the user in
        session.clear()
        session['user_id'] = new_user.id

        # Redirect the user to the appropriate page
        return redirect(url_for('articles.homepage'))
    return render_template('pages/register.html')