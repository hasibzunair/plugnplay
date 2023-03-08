import os
import numpy as np

from PIL import Image

from download import download_file
from clip import load as clip_load
from dino import load as dino_load


LIST_OF_MODELS = {
    "CLIP-RN50": "https://openaipublic.azureedge.net/clip/models/afeb0e10f9e5a86da6080e35cf09123aca3b358a0c3e3b6c78a7b63bc04b6762/RN50.pt",
    "CLIP-ViT-B/32": "https://openaipublic.azureedge.net/clip/models/40d365715913c9da98579312b702a82c18be219cc2a73407c4526f58eba950af/ViT-B-32.pt",
    "DINO-XciT-S12/16": "https://dl.fbaipublicfiles.com/dino/dino_xcit_small_12_p16_pretrain/dino_xcit_small_12_p16_pretrain.pth",
    "DINO-XciT-M24/16": "https://dl.fbaipublicfiles.com/dino/dino_xcit_medium_24_p16_pretrain/dino_xcit_medium_24_p16_pretrain.pth",
    "DINO-ViT-S/16": "https://dl.fbaipublicfiles.com/dino/dino_deitsmall16_pretrain/dino_deitsmall16_pretrain.pth",
    "DINO-ViT-B/16": "https://dl.fbaipublicfiles.com/dino/dino_vitbase16_pretrain/dino_vitbase16_pretrain.pth",
}

# load feat extractor model

def load_feature_extractor(model_name: str, device):
    """
    Loads a feature extractor

    Arguments:
        model_name (str): Name of model

    Returns:
        model (obj): loaded model
        transform (obj): preprocess function

    Examples:
    >>> model, transform = load_feature_extractor("CLIP-RN50", "cpu")
    """

    assert model_name in LIST_OF_MODELS, f"Pick from {LIST_OF_MODELS}"

    model_path = download_file(LIST_OF_MODELS[model_name], os.path.expanduser("~/.cache/models/"))
    print(f"File at {model_path}")

    if model_name.startswith('CLIP'):
        model, transform = clip_load(model_path, device, jit=False)
    elif model_name.startswith('DINO'):
        model, transform = dino_load(model_name, model_path, device)
    return model, transform


# extract features from an image

def get_features(img: np.ndarray, name_of_model:str = "CLIP-RN50", 
                 device:str = "cpu") -> np.ndarray:
    """Extracts features from an image

    Args:
        img (np.ndarray): Input image
        name_of_model (str, optional): Name of pretrained model. Defaults to "CLIP-RN50".
        device (str, optional): GPU or CPU. Defaults to "cpu".

    Returns:
        features (np.ndarray): features of image

    Examples:
    >>> feat = get_features(img, "CLIP-RN50", "cpu") # (1, 1024)
    """
    model, model_transform = load_feature_extractor(name_of_model, device)
    img = Image.fromarray(img)
    # preprocess image
    img = model_transform(img)
    # dummy batch dimension
    img = img.unsqueeze(0).to(device) 
    # get features
    features = model.encode_image(img).cpu().detach().numpy() # throws error w/o .detach(), see why?
    return features