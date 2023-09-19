import glob
import os

from similarity.image_similarity import Img2Vec

if __name__ == '__main__':
    ImgSim = Img2Vec('efficientnet_b3', weights='DEFAULT')

    data_dir = glob.glob(os.path.join('C:/Users/labadmin/Desktop/annoy/downloaded_images', "*", "*", "*.jpg"))
    remove = []
    for data_dir in data_dir:
        remove.append(os.path.abspath(data_dir))
    dataset = ImgSim.embed_dataset(remove)