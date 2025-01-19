from PIL import Image
import numpy as np

def display_pixel_matrix(image_path):
    image = Image.open(image_path)
    image = image.convert("RGB")
    pixel_matrix = np.array(image)
    print("Pixel Matrix of the Image:")
    print(pixel_matrix)
    return pixel_matrix

original_matrix = display_pixel_matrix("inputy.jpeg")  
hidden_matrix = display_pixel_matrix("decryptit.png")


import numpy as np
from PIL import Image

def extract_lsb(image_path):
    # Open the image
    image = Image.open(image_path).convert("RGB")
    # Convert to a NumPy array
    pixel_array = np.array(image)
    # Extract the LSB of each channel
    lsb_array = pixel_array & 1
    print("LSB Matrix:")
    print(lsb_array)  # Print the LSBs of the image
    return lsb_array

# Example usage
original_lsb = extract_lsb("inputy.jpeg")  # Before hiding
hidden_lsb = extract_lsb("decryptit.png")   # After hiding
