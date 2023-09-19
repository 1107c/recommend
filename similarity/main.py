import glob
import os.path
import time

from image_similarity import *
import streamlit as st


if __name__ == '__main__':
    ImgSim = Img2Vec('efficientnet_b3', weights='DEFAULT')


    st.title('Fashion Recommender system')

    upload_img = st.file_uploader('Upload an image', type=['jpg', 'png'])

    if upload_img is not None:
        # 이미지 표시
        st.image(upload_img)
        st.header("file uploaded successfully")
        os.makedirs('C:/Users/labadmin/Desktop/annoy/similarity/uploads', exist_ok=True)
        with open(os.path.join('C:/Users/labadmin/Desktop/annoy/similarity/uploads', upload_img.name), 'wb') as f:
            f.write(upload_img.read())
        data_dir = glob.glob(os.path.join('C:/Users/labadmin/Desktop/annoy/downloaded_images', "*", "*", "*.jpg"))
        remove = []
        for data_dir in data_dir:
            remove.append(os.path.abspath(data_dir))
        dataset = ImgSim.embed_dataset(remove)
        # print(dataset)
        progress_text = "Hold on! Result will shown below."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.02)
            my_bar.progress(percent_complete + 1,
                            text=progress_text)
        file_img=ImgSim.similar_images(os.path.join('C:/Users/labadmin/Desktop/annoy/similarity/uploads',upload_img.name),n=10)
        image_paths = list(file_img.keys())

        col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)

        for index, image_path in enumerate(image_paths):

            if index == 0:
                with col1:
                    st.image(Image.open(image_path))
            elif index == 1:
                with col2:
                    st.image(Image.open(image_path))
            elif index == 2:
                with col3:
                    st.image(Image.open(image_path))
            elif index == 3:
                with col4:
                    st.image(Image.open(image_path))
            elif index == 4:
                with col5:
                    st.image(Image.open(image_path))
            elif index == 5:
                with col6:
                    st.image(Image.open(image_path))
            elif index == 6:
                with col7:
                    st.image(Image.open(image_path))
            elif index == 7:
                with col8:
                    st.image(Image.open(image_path))
            elif index == 8:
                with col9:
                    st.image(Image.open(image_path))
            elif index == 9:
                with col10:
                    st.image(Image.open(image_path))
        else:
            st.header("Some error occured")
