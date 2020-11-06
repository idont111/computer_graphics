import numpy as np
from PIL import Image

black = [0,0,0] # black color
white = [255,255,255] # white color
data = np.loadtxt('myDataSet/DS0.txt', dtype=int) # loading DSO.txt from myDataSet

pixel_data = np.full(shape=(540, 960, 3), fill_value=white, dtype=np.uint8)# creating array with white pixels


pixel_data[539-data[:,0], data[:,1]] = black # cteating black pixels
my_image = Image.fromarray(pixel_data, 'RGB')# using RGB fornat

my_image.show() #show my image
my_image.save('image.png')# save my image
