import numpy as np

def pil_to_numpy(img):
    """
    Convert PIL image to numpy

    Args:
        img (PIL) : input image

    Returns:
        img (np.array) : the output image as numpy array

    Examples:
        >>> img = pil_to_numpy(img)
    """
    img = img.convert("RGB")
    img = np.array(img)
    return img