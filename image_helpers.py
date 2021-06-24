from PIL import Image
import imghdr


def is_grey_scale(img: Image) -> bool:
    """
    Used to separate day and night pictures

    :String file:
    :return: True if image and is greyscale
    """
    w, h = img.size
    diff = 0
    for i in [0, w // 2, w - 1]:
        for j in [0, h // 2, h - 1]:
            r, g, b = img.getpixel((i, j))
            rg = abs(r - g)
            rb = abs(r - b)
            gb = abs(g - b)
            diff += rg + rb + gb;

    return diff < 100


def is_image(file: "") -> bool:
    """
    Separate images from movies and other files

    :param file:
    :return:
    """
    if '.' in file:
        if imghdr.what(file) is not None:
            return True
        else:
            return False
