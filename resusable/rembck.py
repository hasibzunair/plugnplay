from rembg import remove
from PIL import Image

# pip install rembg
# Also see https://huggingface.co/spaces/eugenesiow/remove-bg

def read_image(path):
    return Image.open(path)

def remove_background(image):
    image = remove(image)
    return image
