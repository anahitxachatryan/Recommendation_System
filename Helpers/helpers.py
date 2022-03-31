import os
import random

def show_homePage_randomItem():
    path = 'website/static/Data/styles'
    files = list_files(path)
    choice = random.choice(files)
    return f'../static/Data/styles/{choice}'

def list_files(path):
    return os.listdir(path)
