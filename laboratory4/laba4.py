# imports
import numpy as np
from PIL import Image

white = [255, 255, 255] # white color
red = [255, 0, 0]# red color


def get_perspective_projection(data, vanishing_point=(540, 960), distanse=50):
    '''
    Pillow x, y coords starts with top left angle
    ----------------------
    |(0, 0) (0, 1) (0, 2)|
    |(1, 0) (1, 1) (1, 2)|
    |(2, 0) (2, 1) (2, 2)|
    ---------------------
    '''

    pil_start_point = (540, 0)

    data[:, 0] -= vanishing_point[0] - pil_start_point[0]# shifting X
    data[:, 0] = distanse * data[:, 0] / (distanse + data[:, 2])# transforming X
    data[:, 0] += vanishing_point[0] - pil_start_point[0]# shifting X


    data[:, 1] -= vanishing_point[1] - pil_start_point[1]  # shifting Y
    data[:, 1] = distanse * data[:, 1] / (distanse + data[:, 2]) # transforming Y
    data[:, 1] += vanishing_point[1] - pil_start_point[1] # shifting Y

    return data


def generate_image(figure):
    pixel_image = np.full(shape=(540, 960, 3), fill_value=white, dtype=np.uint8)# creating array with white pixels
    pixel_image[figure[:, 0], figure[:, 1]] = red # drawing red pixels

    return pixel_image



data = np.loadtxt('myDataSet/DS0.txt', dtype=int)

data[:, 0] = 959 - data[:, 0] # mirror inverse y
data = np.insert(data, 2, [100] * len(data), axis=1) # adding new axis z = [100, 100, ..., 100]

get_perspective_projection(data)


my_image = generate_image(data)
new_image = Image.fromarray(my_image, 'RGB')
new_image.show() # showing resulted image
new_image.save('perspectice_projection.png') # saving result to perspectice_projection.png

