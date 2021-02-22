import matplotlib
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread

# Model instantiation
model = ResNet50(weights='imagenet')

img_path = r'C:\Users\ihebd\PycharmProjects\DjangoObjectDetectionApp\pug.jfif'

# read our image
img = imread(img_path)
plt.interactive(True)
print(img)

plt.imshow(img)
plt.waitforbuttonpress()
