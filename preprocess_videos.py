#!/usr/bin/env python3
import argparse
import sys
import video_helpers as vh
import image_helpers as ih
from PIL import Image
import os


def main(argv):
    parser = argparse.ArgumentParser(description="Save video frames to image files and separate day and night images",
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        '-e', '--extraction_interval',
        help='Extract frame every -e seconds. Default: every second (value=1)',
        default=1,
        type=float)
    parser.add_argument(
        '-o', '--outputDir',
        help='Path to the output folder where images should be saved to.'
             'Defaults to the same directory as IMAGEDIR.',
        type=str,
        default='IMAGEDIR'
    )
    args = parser.parse_args()
    if not os.path.exists(args.outputDir):
        os.mkdir(args.outputDir)
    outputDir = args.outputDir
    files = os.listdir()

    for file in files:

        # check if file is video
        if vh.is_video(file):
            print("Found video: " + file)

            # convert video to images
            vh.video2img(file, 10, args.outputDir)


if __name__ == '__main__':
    main(sys.argv)
