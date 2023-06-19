from flask import render_template, redirect, url_for
from app import app, db
from .forms import LoginForm
from .models import User

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # check if user exists and password is correct
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if user.password == form.password.data:
                return redirect(url_for('home'))
    return render_template('login.html', form=form)
