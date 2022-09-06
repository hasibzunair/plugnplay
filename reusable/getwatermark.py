import os
import numpy as np
import torch
import watermark.watermark as watermark

def get_machine_details():
    """
    Get machine details.

    Examples:
        >>> img = numpy_to_pil(img)
    """
    print(watermark())
    print(watermark(iversions=True, globals_=globals()))


if __name__ == "__main__":
    get_machine_details()
