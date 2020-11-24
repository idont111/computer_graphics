import numpy as np
from PIL import Image

# initialization colors
black = [0,0,0] # black color
white = [255,255,255] # white color
blue = [0,0,255]# red color


def affine_transformation(figure, transform_point=(480, 480), angle=np.deg2rad(10)):
    rotation_figure = figure.copy()

    # rotate matrix
    rotation_matrix = np.array([
        [np.cos(angle), np.sin(angle)],
        [-np.sin(angle), np.cos(angle)]
    ])

    rotation_figure -= transform_point # shift to start coordinates
    rotation_figure = rotation_figure @ rotation_matrix# rotation
    rotation_figure += transform_point # shift back

    return np.round(rotation_figure).astype(int)


def generate_image(figure):
    pixel_image = np.full(shape=(960, 960, 3), fill_value=white, dtype=np.uint8)# create array with white pixels
    pixel_image[data[:, 0], data[:, 1]] = black # draw black pixels
    pixel_image[figure[:, 0], figure[:, 1]] = blue # draw red pixels

    return pixel_image



# load data
data = np.loadtxt('myDataSet/DS0.txt', dtype=int)
data[:, 0] = 959 - data[:, 0]

# rotate data
rotation_figure = affine_transformation(data)

# generate image
myimage = generate_image(rotation_figure)

new_img = Image.fromarray(myimage, 'RGB')

new_img.show()# show image
new_img.save('new_image.png')# save image


