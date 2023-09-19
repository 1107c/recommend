import os

from torch.utils.data import Dataset
from PIL import Image
import glob

class CustomDataset(Dataset) :
    def __init__(self, data_dir, transform=None):
        self.data_dir = glob.glob(os.path.join(data_dir,"*", "*", "*.jpg"))

        self.transform = transform
        self.label_dict = self.create_label_dict(data_dir)

    def create_label_dict(self, data_dir):

        label_dict = {}
        for root, dirs, files in os.walk(data_dir):
            if len(dirs) == 0:
                label_name = os.path.basename(root)
                label_dict[label_name] = len(label_dict)

        return label_dict



    def __getitem__(self, item):
        image_path = self.data_dir[item]
        image = Image.open(image_path)
        image = image.convert("RGB")
        label_name = os.path.basename(os.path.dirname(image_path))
        label = self.label_dict[label_name]

        if self.transform is not None :
            image = self.transform(image)

        return image ,label

    def __len__(self):
        return len(self.data_dir)
