import glob
import os
import pickle

from similarity.image_similarity import Img2Vec


def load_data(file_path):
    with open(file_path, 'rb') as file:
        dataset = pickle.load(file)
    return dataset

dataset= load_data('C:/Users/labadmin/Desktop/annoy/dataset.pkl')
print(dataset)