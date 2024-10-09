from PIL import Image
import numpy as np

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / float(width)
    new_height = int(aspect_ratio * new_width)
    return image.resize((new_width, new_height))

def grayscale_image(image): # To grayscale
    return image.convert("L")

def pixels_to_ascii(image): # To ASCII
    pixels = np.array(image)
    ascii_str = ""
    for pixel_row in pixels:
        for pixel in pixel_row:
            ascii_str += ASCII_CHARS[pixel // 32]  # 255 levels of gray divided into 8 (len of ASCII_CHARS)
        ascii_str += "\n"
    return ascii_str

def image_to_ascii(image_path, new_width=100): #MAIN
    try:
        image = Image.open(image_path)
        image = resize_image(image, new_width)
        image = grayscale_image(image)
        
        ascii_str = pixels_to_ascii(image)

        return ascii_str
    except Exception as e: # catch error
        print(f"Error: {e}")
        return None

image_path = input("Enter the path to the image file: ") #input

ascii_art = image_to_ascii(image_path, new_width=100)

if ascii_art: # print
    print(ascii_art)