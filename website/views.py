import pandas as pd
from flask import Blueprint, render_template

from Helpers import helpers
from ML.data_processing import retrieve_most_similar_products as rmsp
from ML.data_processing import read_data

views = Blueprint('views', __name__, template_folder='templates')

@views.route('/')
def home():
    files = read_data("website/static/Data")
    cos_similarities_df = pd.read_csv('ML/cos_similarities.csv')
    cos_similarities_df = cos_similarities_df.set_index('Unnamed: 0')
    img_list = rmsp(cos_similarities_df,f'{files[409]}')

    return render_template(
        "Home.html",
        img_list = list(img_list),
        products = files[409])
    
    
@views.route('/<prod_category>/<prod_name>')
def view_prod(prod_category, prod_name):
    cos_similarities_df = pd.read_csv('ML/cos_similarities.csv')
    cos_similarities_df = cos_similarities_df.set_index('Unnamed: 0')
    path = f'website/static/Data/{prod_category}/{prod_name}'

    img_list = rmsp(cos_similarities_df,f'{path}')
    return render_template(
        "Home.html",
        img_list = img_list,
        products = path)
    
    

@views.route('/catalog')
def catalog():
    item_list =['jewellery','bags','cosmetics']
    randomChoice = []
    for i in range(3):
        randomChoice.append(helpers.catalog_items(item_list[i])[0])

    return render_template(
                            "Catalog.html",
                           randomChoice = randomChoice)


@views.route('/jewellery')
def jewellery():
    randomChoice = helpers.catalog_items('jewellery')
    return render_template(
                            "Catalog.html",
                           randomChoice = randomChoice)


@views.route('/bags')
def bags():
    randomChoice = helpers.catalog_items('bags')
    return render_template(
                            "Catalog.html",
                           randomChoice = randomChoice)

@views.route('/cosmetics')
def cosmetics():
    randomChoice = helpers.catalog_items('cosmetics')
    return render_template(
                            "Catalog.html",
                           randomChoice = randomChoice)


@views.route('/shoes')
def shoes():
    randomChoice = helpers.catalog_items('shoes')
    return render_template(
                            "Catalog.html",
                           randomChoice = randomChoice)
