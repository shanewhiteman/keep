from app import app, db, login_manager
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from forms import RegistrationForm, LoginForm
from models import User

# landing page
@app.route('/')
def index():
    return render_template('index.html')

# registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, email = form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)

# user loader
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

# login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('user_list'))
        else:
            return redirect(url_for('login'))
    
    return render_template('login.html', form=form)

# *for testing* user list
@app.route('/users')
@login_required
def user_list():
    current_users = User.query.all()
    return render_template('user_list.html', current_users = current_users)
