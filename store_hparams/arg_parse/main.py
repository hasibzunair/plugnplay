import argparse
import os
from dotenv import load_dotenv
# https://pypi.org/project/python-dotenv/
# pip install python-dotenv

# Loading environment variables from .env
load_dotenv('config.env')

# Parse
parser = argparse.ArgumentParser(description="Pipepline for ML project.")

parser.add_argument('--batch_size', type=int,
                    required=False, default=0,
                    help='batch_size for the model')

parser.add_argument('--images_dir', type=str,
                    required=False, default=os.environ.get("IMAGES_DIR"),
                    help="Folder containing all the images to analyse")

args = parser.parse_args()


print(args.batch_size)
print(args.images_dir)