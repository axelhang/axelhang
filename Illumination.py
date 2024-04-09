import imageio.v3 as iio
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


images = list()
for file in Path("D:\Master\Python\images").iterdir(): #change path
    if not file.is_file():
        continue

    images.append(iio.imread(file))

#pic = iio.imread('images\PaintTest.png') #imports image


for i in range(len(images)): #range(len(images))
    plt.figure(figsize = (15,15))

    plt.imshow(images[i]) #displays image

    print('Type of the image : ' , type(images[i]))
    print()
    print('Shape of the image : {}'.format(images[i].shape))
    print('Image Hight {}'.format(images[i].shape[0]))
    print('Image Width {}'.format(images[i].shape[1]))
    print('Dimension of Image {}'.format(images[i].ndim))

    print('Image size {}'.format(images[i].size))
    print('Maximum RGB value in this image {}'.format(images[i].max()))
    print('Minimum RGB value in this image {}'.format(images[i].min()))

    gray = lambda rgb : np.dot(rgb[... , :3] , [0.299 , 0.587, 0.114]) #converts to gray scale
    gray = gray(images[i])  

    plt.figure( figsize = (10,10))
    plt.imshow(gray, cmap = plt.get_cmap(name = 'gray'))
    plt.show()

    print(images[0][400][150])
    print(gray[190][0])
    count = 0
    for x in range(images[i].shape[0]):
        for y in range(images[i].shape[1]):
            if gray[x][y] > 220:
                count += 1
    print("Number of illuminated", count)

    ratio = count/(images[i].shape[0]*images[i].shape[1])
    print("Illumination ratio", ratio)