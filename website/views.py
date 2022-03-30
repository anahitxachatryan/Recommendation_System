from flask import Blueprint, render_template

views = Blueprint('views', __name__, template_folder='templates')

@views.route('/')
def home():
    return render_template("Home.html")


@views.route('/catalog')
def catalog():
    return render_template("Catalog.html")