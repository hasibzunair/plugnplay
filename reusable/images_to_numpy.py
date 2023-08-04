import os
import cv2
import numpy as np
from tqdm import tqdm
from PIL import Image
import matplotlib.pyplot as plt

# Assuming Folder Structure
"""
Dataset:
    - Images
        - image_01
        - image_02
        - image_03
"""
# Resize the image
def crop_and_resize(img, resize_dim=1024):
    img = cv2.resize(img, (resize_dim, resize_dim), interpolation=cv2.INTER_AREA)
    return img

# Read images and convert it to RGB
def get_data(images):
    img = cv2.imread(images)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
    img = crop_and_resize(img)
    return img

# Load images and convert it to numpy
def convert_to_numpy(path):
    print(path)
    folder_name = os.path.basename(path)  # Get the folder name
    inp_feat = []
    image_files = os.listdir(path)
    for file_name in tqdm(image_files):
        file_path = os.path.join(path, file_name)
        img = get_data(file_path)
        inp_feat.append(img)

    inp_feat = np.array(inp_feat)
    print(inp_feat.shape)
    np.save(f"{folder_name}.npy", inp_feat)  # Save the .npy file with the folder name
    print("Done!")

def main() -> None:

    data_path = "./Datasett/"

    image_path = os.path.join(data_path, "Images")

    convert_to_numpy(image_path)



"""Optional"""

def single_image(data):
    image_data = data.reshape(1024,1024,3)
    pil_image = Image.fromarray(image_data)
    plt.imshow(pil_image)


def show_multiple_images(data):
  row = 1
  columns = len(image_data)
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


if __name__ == "__main__":
    main()
    
    """if you want to see your converted .npy file as image."""
    image_data = np.load("Images.npy")
    
    if image_data.shape[0] == 1:
        single_image(image_data)
    else:
        show_multiple_images(image_data)