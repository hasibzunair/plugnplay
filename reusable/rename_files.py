import os
import glob

"""Rename files in a folder."""

# rename images in a dir
IMAGES_FOLDER = "../datasets/basketball_datasetv0/images/train/"
imgs = sorted(glob.glob(IMAGES_FOLDER + "/" + "/*.jpg"))
for number in os.listdir(IMAGES_FOLDER)[:]:
    # print(number)
    nn = IMAGES_FOLDER + "train" + number
    # print(nn)
    on = IMAGES_FOLDER + number
    # print(on)
    os.rename(on, nn)
