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
                if cell_height >= 1 and cell_width >= 1:  # Check cell size
                    image = img[int(i * cell_height):int((i + 1) * cell_height),
                               int(j * cell_width):int((j + 1) * cell_width)]
                    index = int(np.mean(image) / 255 * len(char_list))
                    f.write(char_list[index])
                else:
                    print(f"Error: Cell size is too small ({cell_width}, {cell_height})")
            except Exception as e:  # Catch specific exceptions for better error handling
                print(f"Error processing cell ({i}, {j}): {e}")
        f.write("\n")

# Handle the last row if necessary
if rows * cell_height < h:
    last_row_start = rows * cell_height
    last_row_end = h
    for j in range(cols):
        try:
            image = img[last_row_start:last_row_end, int(j * cell_width):int((j + 1) * cell_width)]
            index = int(np.mean(image) / 255 * len(char_list))
            f.write(char_list[index])
        except Exception as e:
            print(f"Error processing last row cell ({rows}, {j}): {e}")
    f.write("\n")
    
