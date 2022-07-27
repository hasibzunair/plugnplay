import numpy as np
import cv2
from PIL import Image, ImageOps

# Code commenting reference:
# https://github.com/hasibzunair/res-unet-fastmri/blob/master/fastMRI/data/transforms.py

def resize_image(image_path, new_width=192, new_height=256):
    """ 
    Load and resize an image to a desired size.

    Arguments:
        image_path (str): Image to load and resize
        new_width (int): New width of the image
        new_height (int): New height of the image

    Returns:
        img (np.array): Resized image
    """
    assert type(image_path) == str, f"Should be a path, got: {image_path} which is {type(image_path)}"
    
    img = Image.open(image_path)
    img = ImageOps.fit(image_path, (new_width, new_height), Image.BICUBIC)
    img = img.convert("RGB")
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    # If need saving
    # using cv2
    #cv2.imwrite("path.png", img)
    # or using PIL
    # img.save("path.png")
    return img