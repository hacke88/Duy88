import numpy as np
import cv2

char_list = "$@B%8&WM#*oahkbdpqwmZO@QL.CJ"

img = cv2.imread("Image.jpeg")
cols = 300  # Assign the value to cols

h, w, c = img.shape  # Assign image dimensions

cell_width = h / cols
cell_height = cell_width * 2
rows = int(h / cell_height)

with open("Image_file.txt", "a") as f:  # Use with statement for automatic closing
    for i in range(rows):
        for j in range(cols):
            try:
                image = img[int(i * cell_height):int((i + 1) * cell_height),
                           int(j * cell_width):int((j + 1) * cell_width)]
                index = int(np.mean(image) / 255 * len(char_list))
                f.write(char_list[index])
            except:
                pass
        f.write("\n")
       