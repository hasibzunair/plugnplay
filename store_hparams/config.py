import numpy as np

# Dataset params
DATA_DIR = "/projects/secret_project/dataset/"
NORMALISE_PARAMS = [
    1.0 / 255,  # SCALE
    np.array([0.485, 0.456, 0.406]).reshape((1, 1, 3)),  # MEAN
    np.array([0.229, 0.224, 0.225]).reshape((1, 1, 3)),  # STD
]

# Network params
PRETRAINED = True

# Optimizer params
OPTIM = "sgd"
LR = 1e-4
