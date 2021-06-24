import cv2
import ntpath


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


def getFrame(video, frame_at_second, output_path, image_basename, image_identifier):
    """
    Extracts and saves a frame at a given second to a file
    :param video:
    :param frame_at_second: extract the frame at the given second
    :param output_path:
    :param image_basename:
    :param image_identifier:
    :return:
    """
    video.set(cv2.CAP_PROP_POS_MSEC, frame_at_second * 1000)
    hasFrames, frame = video.read()
    if hasFrames:
        cv2.imwrite(output_path + "/" + image_basename + "_" + str(image_identifier) + ".jpg",
                    frame)  # save frame as JPG file
    return hasFrames


def video2img(file, extraction_interval, output_path, image_basename=""):
    """
    Extract frames from a video and save 'em to image files

    :param file:
    :param extraction_interval: seconds between frame extractions
    :param output_path:
    :param image_basename: name of the output images where the identifier is added, if not given, the name of the video
    is used
    :return: True if successful
    """
    video = cv2.VideoCapture(file)

    if not image_basename:
        image_basename = ntpath.basename(file.split(".")[0])

    frame_iterator = 0
    image_identifier = 1
    is_frame = getFrame(video, frame_iterator, output_path, image_basename, image_identifier)
    while is_frame:
        image_identifier = image_identifier + 1
        frame_iterator = frame_iterator + extraction_interval
        frame_iterator = round(frame_iterator, 2)
        is_frame = getFrame(video, frame_iterator, output_path, image_basename, image_identifier)
