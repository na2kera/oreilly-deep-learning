import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread("icon.jpg")
plt.imshow(img)
plt.show()