from rembg import remove
from PIL import Image

# pip install rembg
# Also see https://huggingface.co/spaces/eugenesiow/remove-bg

def read_image(path):
    return Image.open(path)

def remove_background(image):
    image = remove(image)

    # To save, do:
    # image.save("name.png")
    
    # For black background: 
    # cv2.imwrite("name.png", cv2.cvtColor(np.array(a.convert("RGB")), cv2.COLOR_RGB2BGR))
    return image

