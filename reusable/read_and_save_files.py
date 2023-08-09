import os
import shutil

"""Script that saves all image and video files from different folders into a new directory."""

def save_images(source_dir, destination_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Iterate through all the folders and files in the source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Check if the file is an image file
            if file.lower().endswith(('.HEIC', '.mov', '.MP4', '.mp4' '.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                # Get the full path of the source file
                source_file = os.path.join(root, file)
                # Get the full path of the destination file
                destination_file = os.path.join(destination_dir, file)
                # Copy the image file to the destination directory
                shutil.copy2(source_file, destination_file)

# Example usage
source_directory = './my_gphotos'
destination_directory = './gphotos'

save_images(source_directory, destination_directory)