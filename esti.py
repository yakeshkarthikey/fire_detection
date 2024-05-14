
from roboflow import Roboflow

rf = Roboflow(api_key="U7bCjidgxGa0MXSp4uRR")
project = rf.workspace().project("fire-detection-4tf8l")
model = project.version(5).model

from skimage.io import imread,imshow 

img = "color_img.jpg"
p = model.predict(img).json()


p1 = p["predictions"]

print(p1)


print()

model.predict(img).save("prediction.jpg")



img = imread("prediction.jpg")
imshow(img)


