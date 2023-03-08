import os
import urllib.request
import tqdm 

def download_file(url: str, root:str = os.path.expanduser("~/.cache/models")):
    """
    Downloads a file from a URL and save it in a defined folder.
    
    Arguments:
        url (str): URL to download
        root (str): directory to save file
    
    Returns:
        None

    Examples:
        >>> download_file("URL", "PATH_TO_SAVE")
    """
    os.makedirs(root, exist_ok=True)
    filename = os.path.basename(url)
    download_target = os.path.join(root, filename)

    if os.path.exists(download_target) and os.path.isfile(download_target):
        return download_target
    print(f"Downloading model from {url}")

    urllib.request.urlretrieve(url, download_target)
    return download_target
