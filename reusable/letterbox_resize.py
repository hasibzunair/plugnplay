import cv2 
import numpy as np

def letterbox(img: np.ndarray, new_shape:int = 640) -> np.ndarray:
    """
    Resizes and image while maintaining aspect ratio. Also known as letterbox resizing.

    Arguments:
        img (np.array): input image
        new_shape (int): size of new image

    Returns:
        img (str): new image

    Examples:
    >>> img = letterbox(img, (224, 224))
    """
    assert type(img) == np.ndarray, f"Image should be numpy array."
    assert type(new_shape) == int, f"Should be integer."

    H, W = img.shape[:2]
    if isinstance(new_shape, int):
        new_shape = (new_shape, new_shape)

    r = min(new_shape[0] / H, new_shape[1] / W)
    nH, nW = round(H * r), round(W * r)
    pH, pW = np.mod(new_shape[0] - nH, 32) / 2, np.mod(new_shape[1] - nW, 32) / 2

    if (H, W) != (nH, nW):
        img = cv2.resize(img, (nW, nH), interpolation=cv2.INTER_LINEAR)

    top, bottom = round(pH - 0.1), round(pH + 0.1)
    left, right = round(pW - 0.1), round(pW + 0.1)
    img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=(114, 114, 114))
    return img