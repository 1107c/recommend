import os
import shutil
from sklearn.model_selection import train_test_split
from tqdm import tqdm

# 최상위 디렉토리
root_dir = 'downloaded_images'

# 학습용(train)과 검증용(val) 데이터셋을 저장할 디렉토리 생성
train_dir = './data/train_images'
val_dir = './data/val_images'

os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# 디렉토리 구조를 순회하면서 이미지 데이터 수집
for folder_name in tqdm(os.listdir(root_dir)):
    folder_path = os.path.join(root_dir, folder_name)
    if os.path.isdir(folder_path):
        # 폴더 이름을 사용하여 train과 val을 나누기 위한 경로 생성
        train_folder = os.path.join(train_dir, folder_name)
        val_folder = os.path.join(val_dir, folder_name)

        os.makedirs(train_folder, exist_ok=True)
        os.makedirs(val_folder, exist_ok=True)

        # 하위 폴더 순회
        for subfolder_name in tqdm(os.listdir(folder_path)):
            subfolder_path = os.path.join(folder_path, subfolder_name)
            if os.path.isdir(subfolder_path):
                # 이미지 파일 목록 가져오기
                image_files = [file for file in os.listdir(subfolder_path) if file.endswith(".jpg")]

                # 이미지 데이터를 학습용과 검증용으로 나누기
                train_images, val_images = train_test_split(image_files, test_size=0.2, random_state=42)

                # 학습용 이미지를 해당 폴더로 복사
                for image in tqdm(train_images, leave=False):
                    src = os.path.join(subfolder_path, image)
                    dst = os.path.join(train_folder, subfolder_name, image)
                    os.makedirs(os.path.dirname(dst), exist_ok=True)
                    shutil.copy(src, dst)

                # 검증용 이미지를 해당 폴더로 복사
                for image in tqdm(val_images, leave=False):
                    src = os.path.join(subfolder_path, image)
                    dst = os.path.join(val_folder, subfolder_name, image)
                    os.makedirs(os.path.dirname(dst), exist_ok=True)
                    shutil.copy(src, dst)
