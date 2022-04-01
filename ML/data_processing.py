import os
import numpy as np
import pandas as pd
import itertools

from keras.applications import vgg16
from keras.models import Model
from tensorflow import keras
from keras.preprocessing.image import load_img,img_to_array
from keras.applications.imagenet_utils import preprocess_input
from sklearn.metrics.pairwise import cosine_similarity

import matplotlib.pyplot as plt

def read_data(img_path):
    dirs = os.listdir(img_path)

    files = []
    for dir in dirs:
        fullDir = f'{img_path}/{dir}/'
        foundImgs = [fullDir + x for x in os.listdir(fullDir) if 'png' in x]
        files.append(foundImgs)
    files = list(itertools.chain(*files))
    return files


def create_model():
    vgg_model = vgg16.VGG16(weights='imagenet')
    feat_extractor = Model(inputs=vgg_model.input, outputs=vgg_model.get_layer("fc2").output)
    feat_extractor.save('model')



def process_all_imgs(files):
    importedImages = []

    for f in files:
        filename = f
        original = load_img(filename, target_size=(224, 224))
        numpy_image = img_to_array(original)
        image_batch = np.expand_dims(numpy_image, axis=0)
        importedImages.append(image_batch)
    images = np.vstack(importedImages)

    processed_imgs = preprocess_input(images.copy())
    return processed_imgs

def extract_features(processed_imgs, feat_extractor):
    imgs_features = feat_extractor.predict(processed_imgs)
    return imgs_features

def create_csv_based_on_similarity(imgs_features,files):
    cosSimilarities = cosine_similarity(imgs_features)
    cos_similarities_df = pd.DataFrame(cosSimilarities, columns=files, index=files)
    return cos_similarities_df



def retrieve_most_similar_products(cos_similarities_df,given_img,imgs_model_width=224,imgs_model_height=224,nb_closest_images=3):
    img_list = []
    original = load_img(given_img, target_size=(224, 224))
    closest_imgs = cos_similarities_df[given_img].sort_values(ascending=False)[1:nb_closest_images+1].index
    closest_imgs_scores = cos_similarities_df[given_img].sort_values(ascending=False)[1:nb_closest_images+1]


    for i in range(0,len(closest_imgs)):
        similar = load_img(closest_imgs[i], target_size=(imgs_model_width, imgs_model_height))
        img_list.append(similar)
    return img_list


def retrain_model():
    files = read_data("../website/static/Data")
    feat_extractor = keras.models.load_model('model')
    processed_imgs = process_all_imgs(files)
    imgs_features = extract_features(processed_imgs, feat_extractor)
    cos_similarities_df = create_csv_based_on_similarity(imgs_features,files)
    cos_similarities_df.to_csv('cos_similarities.csv')

retrain_model()





