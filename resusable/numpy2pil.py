import numpy as np
from PIL import Image

def numpy_to_pil(img):
    """
    Convert numpy image to PIL

    Args:
        img (np.array) : input image

    Returns:
        img (PIL) : the output image as numpy array

    Examples:
        >>> img = numpy_to_pil(img)
    """
    img = Image.fromarray(np.uint8(img)).convert('RGB')
    # If need saving
    # or using PIL - img.save("path.png")
    return img