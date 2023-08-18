import os
import cv2
import argparse
import numpy as np
from tqdm import tqdm
from PIL import Image
import matplotlib.pyplot as plt

"""
Script to convert a folder of images into numpy format.

Folder structure for images:

- Images
    - image_01
    - image_02
    - image_03

Usage:
python images_to_numpy.py --image_path "./images" --saved_file_name "to_numpy" 
python images_to_numpy.py --image_path "./images" --saved_file_name "to_numpy" --visualize yes --visualize_for multiple 
"""

parser = argparse.ArgumentParser(description= 'Convert images to numpy array')
parser.add_argument('--image_path', type= str, required = True, default= "Images", help = 'Set images path.')
parser.add_argument('--saved_file_name', type= str, required= True, default= "images_to_nparray", help = 'Define saved file name.')
parser.add_argument('--visualize', type= str, choices= ['no', 'yes'], default= "no", required = False, help = 'Visualize images.')
parser.add_argument('--visualize_for', type= str, choices= ['single', 'multiple', "no"], default = "no", required = False, help = 'Choose Visualize for single/multiple images.')

args = parser.parse_args()


def crop_and_resize(img, resize_dim = 256):
    """
    Resize the input image.
    
    Aurguments:
        img: Orginal input image
        resized_dim: Size of new image (Default: 256)
    
    Returns:
        img: new image
    """
    img = cv2.resize(img, (resize_dim, resize_dim), interpolation=cv2.INTER_AREA)
    return img

def get_data(image_path, image_file):
    """
    Read images and convert it to RGB. By default OpenCV read images in BGR format.

    Aurguments:
        image_path: input image path
        image_file: input image files

    Returns:
        img: RGB image

    """
    images = os.path.join(image_path, image_file)
    img = cv2.imread(images)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = crop_and_resize(img)
    return img

def convert_to_numpy(path) -> None:
    """
   Load images and convert it to numpy

    Aurguments:
        path: input image path

    Returns:
        None

    """
    inp_feat = []
    image_files = os.listdir(path)
    for file_name in tqdm(image_files):
        img = get_data(path, file_name)
        inp_feat.append(img)

    inp_feat = np.array(inp_feat)
    print(inp_feat.shape)
    np.save(f"{args.saved_file_name}.npy", inp_feat)  # Save the .npy file with the folder name
    print("Done!")


def visualize(data):
    """
    (Optional) 
    Visualization of ndarray as Images. 
    """
    if args.visualize_for == "single":
        try:
            image_data = data.reshape(256,256,3)
            pil_image = Image.fromarray(image_data)
            plt.imshow(pil_image)
            plt.show()
        except:
            print(f"Failed to Show!! You have multiple images in your npy file. Used --visualize_for multiple")
    else:
        try:
            row = 1
            columns = len(data)
            fig, axarr = plt.subplots(row, columns, figsize=(15, 5))

            for i, img_array in tqdm(enumerate(data)):
                # Convert it to Image
                to_image = Image.fromarray(img_array)
                # Display each image on its corresponding subplot
                axarr[i].imshow(to_image)
            
            # Remove the extra empty subplots (if any)
            for i in range(len(data), row * columns):
                fig.delaxes(axarr.flatten()[i])

            plt.tight_layout()
            plt.show()
        except:
            print(f"Falied to Show!!! You have single image in your npy file. Used --visualize_for single")
def main() -> None:

    convert_to_numpy(args.image_path)

if __name__ == "__main__":
    main()
    
    if args.visualize == 'no':
        print("Nothing to Show!!")
    else:
        """if you want to visualize your converted .npy file as image."""
        converted_image_data = np.load(args.saved_file_name + '.npy')
        visualize(converted_image_data)
        