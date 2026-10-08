# THIS VIDEO_UTILS IS GOING TO HAVE THE UTILITY TO READ THE VIDEO QAND SAVE THE VIDEO

import cv2

#Listing the frames in the list
def read_video(video_path):
    cap = cv2.VideoCapture(video_path)   # It takes video file of images of camera index. 
    frames = []
    while True:
        ret, frame = cap.read()  # Read and decode the frame.
        if not ret:
            break
        frames.append(frame)
    return frames

#
def save_video(output_video_frames, output_video_path):
    #VideoWriter_fourcc converts four-character code into integer, XVID a popular codec for vido compression, * character is used to
    #unpack the string 'XVID'
    fourcc = cv2.VideoWriter_fourcc(*'XVID')   #Definig the output format
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (output_video_frames[0].shape[1], output_video_frames[0].shape[0]))  
    for frame in output_video_frames:
        out.write(frame)
    out.release()
