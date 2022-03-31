from flask import Blueprint, render_template

from Helpers import helpers
views = Blueprint('views', __name__, template_folder='templates')

@views.route('/')
def home():
    randomChoice = helpers.show_homePage_randomItem()
    return render_template("Home.html", randomChoice = randomChoice)


@views.route('/catalog')
def catalog():
    return render_template("Catalog.html")