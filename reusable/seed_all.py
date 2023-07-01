def seed_everything(seed: int):
    """Seed everything for reproducibility.

    Args:
        seed (int): integer for defining seed.

    Returns:
        None
    
    Examples:
        >>> seed_everything(42)
    """
    import random, os
    import numpy as np
    import torch
    
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(0)
    if torch.cuda.is_available():
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = True