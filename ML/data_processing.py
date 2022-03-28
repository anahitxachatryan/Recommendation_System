import os
import numpy as np
import pandas as pd

from keras.applications import vgg16
from keras.models import Model
from keras.preprocessing.image import load_img,img_to_array
from keras.applications.imagenet_utils import preprocess_input
from sklearn.metrics.pairwise import cosine_similarity


def read_data(img_path):
    files = [img_path + x for x in os.listdir(img_path) if 'png' in x]
    return files


def create_model():
    vgg_model = vgg16.VGG16(weights='imagenet')
    feat_extractor = Model(inputs=vgg_model.input,outputs = vgg_model.get_layer('fc2').output)
    return feat_extractor


def process_all_imgs(files):
    importedImages = []
    for f in files:
        filename = f
        og = load_img(filename,target_size=(224,224))
        numpy_img = img_to_array(og)
        image_batch = np.expand_dims(numpy_img,axis=0)
        importedImages.append(image_batch)
    images = np.vstack(importedImages)
    processed_image = preprocess_input(images.copy())
    return processed_image


def create_csv_basedOn_similarity(img_path):
    files = read_data(img_path)
    processed_image = process_all_imgs(files)
    feat_extractor = create_model()
    imgs_features = feat_extractor.predict(processed_image)

    cosSimilarities = cosine_similarity(imgs_features)
    cos_similarities_df = pd.DataFrame(cosSimilarities, columns=files, index=files)
    return cos_similarities_df

print(create_csv_basedOn_similarity("../Data/styles/"))