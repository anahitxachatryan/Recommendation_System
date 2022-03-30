from flask import Blueprint, render_template

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/login')
def login():
    return render_template("Login.html")


@auth.route('/logout')
def logout():
    return "<p>logout</p>"


@auth.route('/signup')
def signup():
    return "<p>signup</p>"