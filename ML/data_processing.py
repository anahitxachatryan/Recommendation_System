import os
import numpy as np

from keras.applications import vgg16
from keras.models import Model
from keras.preprocessing.image import load_img,img_to_array
from keras.applications.imagenet_utils import preprocess_input

def read_data(img_path):
    files = [img_path + x for x in os.listdir(img_path) if 'png' in x]
    return files

def create_model():
    vgg_model = vgg16.VGG16(weights='imagenet')
    feat_extractor = Model(inputs=vgg_model.input,outputs = vgg_model.get_layer('fc2').output)
    return feat_extractor