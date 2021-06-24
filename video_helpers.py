def is_video(file: "") -> bool:
    """
    Check if file is a video
    :param file:
    :return:
    """
    if file.endswith(".avi") or file.endswith(".AVI"):
        return True
    else:
        return False
