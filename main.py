import image_helpers as ih
import os
from PIL import Image


def main():
    folder = "test_data"
    files = os.listdir(folder)
    files = [folder + "/" + f for f in files]
    for file in files:

        if ih.is_image(file):
            img = Image.open(file).convert('RGB')
            print(ih.is_grey_scale(img))


if __name__ == '__main__':
    main()
