""" The extract_frame.py is part of the data preprocessing of
our dataset that aims to transfer raw videos for both vision and
touch into static frames to support further applications. Specifically,
Two folders "video_frames" and "gelsight_frame" will be generated.
To run this code, please change the dir in line 57 to the path of our dataset.
"""
import os
from pathlib import Path
import numpy as np
import cv2

def getfiles(dir):
    filenames = os.listdir(dir)
    return filenames

def merge(dir):
    video1_dir = str(dir) + '/' + 'video.mp4'
    video2_dir = str(dir) + '/' + 'gelsight.mp4'

    cap1 = cv2.VideoCapture(video1_dir)
    frame_number1 = int(cap1.get(7))

    cap2 = cv2.VideoCapture(video2_dir)
    frame_number2 = int(cap2.get(7))

    frame_number1 = min(frame_number1, frame_number2)

    # if processed previously, skip this video
    if os.path.exists(str(dir) + '/vision'):
        return

    if not os.path.exists(str(dir) + '/vision'):
        os.makedirs(str(dir) + '/vision')
    if not os.path.exists(str(dir) + '/tactile'):
        os.makedirs(str(dir) + '/tactile')

    for i in range(frame_number1):
        cap1.set(cv2.CAP_PROP_POS_FRAMES, i)
        cap2.set(cv2.CAP_PROP_POS_FRAMES, i)
        _, frame1 = cap1.read()
        _, frame2 = cap2.read()
        cv2.imwrite(str(dir) + '/vision/' + str(i).rjust(10, '0') + '.jpg', frame1)
        cv2.imwrite(str(dir) + '/tactile/' + str(i).rjust(10, '0') + '.jpg', frame2)

    cap1.release()
    cap2.release()

    # Delete the original video files after processing
    if os.path.exists(video1_dir):
        os.remove(video1_dir)
        print(f"Deleted {video1_dir}")
    if os.path.exists(video2_dir):
        os.remove(video2_dir)
        print(f"Deleted {video2_dir}")

def main():
    dir = Path('/root/autodl-tmp/tvl/Touch-Vision-Language-Dataset/tag/touch_and_go/dataset/')  # Path to dataset
    files = getfiles(dir)
    if '.DS_Store' in files:
        files.remove('.DS_Store')

    for i in range(len(files)):
        sub_dir = Path(str(dir) + '/' + (files[i]))
        print(str(sub_dir) + " Start!")
        merge(sub_dir)
        print(str(sub_dir) + " Finished!")

if __name__ == '__main__':
    main()
