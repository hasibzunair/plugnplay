from PIL import Image
from torchvision.transforms import Compose, Resize, CenterCrop, ToTensor, Normalize

try:
    from torchvision.transforms import InterpolationMode

    BICUBIC = InterpolationMode.BICUBIC
except ImportError:
    BICUBIC = Image.BICUBIC


def _convert_image_to_rgb(image):
    return image.convert("RGB")


def resize_center_crop(img):
    """ 
    Load and resize an image to a desired size.

    Arguments:
        img (PIL image): Image to load and resize

    Returns:
        img (np.array): Resized and cropped image

    Examples:
        >>> img = resize_center_crop(img)
    """

    if type(img) == str:
        img = Image.open(img)

    transform = Compose(
        [
            Resize(224, BICUBIC),
            CenterCrop(224),
            _convert_image_to_rgb,
            # ToTensor(),
            # Normalize(
            #     (0.5, 0.5, 0.5),
            #     (0.5, 0.5, 0.5),
            # ),
        ]
    )
    img = transform(img)
    #img = np.array(img)
    return img

