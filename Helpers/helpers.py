import os
import random
import itertools


def show_homePage_randomItem():
    randomChoice_list = []
    path = 'website/static/Data'
    files = list_files(path)

    for file in files:
        temp = list_files(f'{path}/{file}')
        temp =[f'../static/Data/{file}/' + sub for sub in temp]
        randomChoice_list.append(temp)
    randomChoice_list = [val for sublist in randomChoice_list for val in sublist]

    randomChoice = random.choice(randomChoice_list)
    return randomChoice


def list_files(path):
    return os.listdir(path)


def catalog_items(catalogItem):
    randomChoice_list = []
    path = f'website/static/Data/{catalogItem}'
    files = list_files(path)
    for i in range(3):
        str = f'../static/Data/{catalogItem}/'+random.choice(files)
        randomChoice_list.append(str)
    return randomChoice_list