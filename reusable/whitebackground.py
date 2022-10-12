from rembg import remove
from PIL import Image

# pip install rembg==2.0.25

def read_image(path):
    return Image.open(path)

def white_background(image):
    """
    Remove background from image and add white background

    Arguments:
        image (PIL or numpy) : input image
    
    Returns
        image (PIL or numpy) : image with background removed

    Example:
        >>> image = white_background(image)
    """
    assert len(image.size) == 2, f"Should be a path, got: {image} which is {type(image)}"
    
    mask = remove(
        image, alpha_matting=True, alpha_matting_erode_size=15, only_mask=True
    ).convert("L")
    empty = Image.new("RGBA", (image.size), (255, 255, 255))
    image = Image.composite(image, empty, mask)

    # To save, do:
    # image.save("name.png")
    
    # For black background: 
    # cv2.imwrite("name.png", cv2.cvtColor(np.array(a.convert("RGB")), cv2.COLOR_RGB2BGR))
    return image

