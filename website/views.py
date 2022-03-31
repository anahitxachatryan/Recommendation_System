from flask import Blueprint, render_template

from Helpers import helpers
views = Blueprint('views', __name__, template_folder='templates')

@views.route('/')
def home():
    return render_template("Home.html")


@views.route('/catalog')
def catalog():
    randomChoice0 = helpers.catalog_items('jewellery')
    randomChoice1 = helpers.catalog_items('bags')
    randomChoice2 = helpers.catalog_items('cosmetics')
    return render_template(
                            "Catalog.html",
                           randomChoice0=randomChoice0[0],
                           randomChoice1=randomChoice1[0],
                           randomChoice2=randomChoice2[0])


@views.route('/jewellery')
def jewellery():
    randomChoice = helpers.catalog_items('jewellery')
    return render_template(
                            "Catalog.html",
                           randomChoice0=randomChoice[0],
                           randomChoice1=randomChoice[1],
                           randomChoice2=randomChoice[2])


@views.route('/bags')
def bags():
    randomChoice = helpers.catalog_items('bags')
    return render_template(
                            "Catalog.html",
                           randomChoice0=randomChoice[0],
                           randomChoice1=randomChoice[1],
                           randomChoice2=randomChoice[2])

@views.route('/cosmetics')
def cosmetics():
    randomChoice = helpers.catalog_items('cosmetics')
    return render_template(
                            "Catalog.html",
                           randomChoice0=randomChoice[0],
                           randomChoice1=randomChoice[1],
                           randomChoice2=randomChoice[2])


@views.route('/shoes')
def shoes():
    randomChoice = helpers.catalog_items('shoes')
    return render_template(
                            "Catalog.html",
                           randomChoice0=randomChoice[0],
                           randomChoice1=randomChoice[1],
                           randomChoice2=randomChoice[2])
