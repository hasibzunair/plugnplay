import os
import glob 
from natsort import natsorted

# Sort files using natsorted, see more https://pypi.org/project/natsort/.

folder = os.path.join("./dataset/images/")
files = natsorted(glob.glob(folder+ "/" + "/*.jpg"))