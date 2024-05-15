import imageio.v3 as iio
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import cv2


images = list()
for file in Path(r"C:\Users\hanga\Documents\Master\Python\Images").iterdir(): #change path
    if not file.is_file():
        continue

    images.append(iio.imread(file))

#pic = iio.imread('images\PaintTest.png') #imports image

def focus_average_brightness(focus_center, focus_width, gray_scale): #calculate average brightness in focus 
    upper = focus_center - focus_width/2
    lower = focus_center + focus_width/2
    total_brightness = 0
    average = 0
    for x in range(int(upper), int(lower)):
        for y in range(images[i].shape[1]):
            total_brightness += gray_scale[x][y]
    average = total_brightness/((lower-upper)*images[i].shape[1])
    return average

def light_scatter_plot(focus_center, focus_width, gray_scale): #plots average brightness in y dir
    row_tot = 0
    average_row_list = np.zeros(images[i].shape[0])
    pos = list(range(0, images[i].shape[0]))
    for k in range(images[i].shape[0]):
        for j in range(images[i].shape[1]):
            row_tot += gray_scale[k][j]
        average_row_list[k] = (row_tot/images[i].shape[1])
        row_tot = 0
    
    upper = focus_center - focus_width/2
    lower = focus_center + focus_width/2

    plt.plot(pos, average_row_list)
    plt.show()



def warp_image(images): #legg inn farge kryss for start koordinater
    image = images[i]
    src_points = np.float32([[0, 0], [image.shape[1] - 1, 0], [0, image.shape[0] - 1], [image.shape[1] - 1, image.shape[0] - 1]]) 
    dst_points = np.float32([[100, 100], [image.shape[1] - 100, 100], [0, image.shape[0] - 1], [image.shape[1] - 1, image.shape[0] - 1]]) 
  
    matrix = cv2.getPerspectiveTransform(src_points, dst_points) 

    warped_image = cv2.warpPerspective(image, matrix, (image.shape[1], image.shape[0])) 

    cv2.imshow('Original Image', image) 
    cv2.imshow('Warped Image', warped_image) 
    cv2.waitKey(0) 
    cv2.destroyAllWindows()

    return warped_image

for i in range(len(images)): #range(len(images))
    #plt.figure(figsize = (8,8))

    #plt.imshow(images[i]) #displays image

    #print('Type of the image : ' , type(images[i]))
    #print()
    #print('Shape of the image : {}'.format(images[i].shape))
    print('Image Hight {}'.format(images[i].shape[0]))
    print('Image Width {}'.format(images[i].shape[1]))
    #print('Dimension of Image {}'.format(images[i].ndim))

    #print('Image size {}'.format(images[i].size))
    print('Maximum RGB value in this image {}'.format(images[i].max()))
    print('Minimum RGB value in this image {}'.format(images[i].min()))

    images[i] = warp_image(images)
    gray = lambda rgb : np.dot(rgb[... , :3] , [0.299 , 0.587, 0.114]) #converts to gray scale
    gray = gray(images[i])  
    
    plt.figure( figsize = (8,8))
    plt.imshow(gray, cmap = plt.get_cmap(name = 'gray'))
    plt.show()

    #print(images[0][400][150])
    #print(gray[190][0])
    count = 0
    for x in range(images[i].shape[0]):
        for y in range(images[i].shape[1]):
            if gray[x][y] > 220:
                count += 1
    print("Number of illuminated", count)

    ratio = count/(images[i].shape[0]*images[i].shape[1])
    print("Illumination ratio", ratio)

    print("Average brightness in focus", focus_average_brightness(images[i].shape[0]/2, 100, gray))
    
    light_scatter_plot(images[i].shape[0]/2, 100, gray)
