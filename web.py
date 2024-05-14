import streamlit as st 
import cv2
from PIL import Image
import numpy as np
from skimage.io import imread,imshow,imsave
from roboflow import Roboflow
import subprocess 

def yolo(image):
    def execute_python_file(file_path):
        try:
            completed_process = subprocess.run(['python', file_path], capture_output=True, text=True)
            if completed_process.returncode == 0:
                print("Execution successful.")
                print("Output:")
                print(completed_process.stdout)
                st.write(completed_process.stdout)
            else:
                print(f"Error: Failed to execute '{file_path}'.")
                print("Error output:")
                print(completed_process.stderr)
                
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' does not exist.")

    file_path = 'esti.py'
    execute_python_file(file_path)

    img = imread("prediction.jpg")
    st.image(img)

def start(file):
    import cv2
    from skimage.util import img_as_ubyte
    img_file_buffer = file
    image = imread(img_file_buffer)
    st.write("input image")
    st.image(image)
    img_ubyte = img_as_ubyte(image)# if you want to pass it to OpenCV
    img = 'color_img.jpg'
    imsave(img, img_ubyte)
    # st.image(image, caption="The caption", use_column_width=True)
    # array = np.reshape(img_array, (128, 128))

    if file:
        st.info("file entered")
        st.image(file)

    button = st.button('Enter')

    if button:
        yolo(img)
        

st.title("Fire Alert System")

st.subheader("Enter your Image")

home, info = st.tabs(["Home","Info"])

with home:
    file = st.file_uploader("enter the image")
    st.write(file)
    print(file)

    try:
        start(file)
    except:
        pass
with info:
    st.write("A initial level fire alert system project")
