from freenect import sync_get_depth as get_depth, sync_get_video as get_video
import cv2
import mediapipe as mp
import numpy as np
import signal  

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

keep_running = True

def doloop():
    global depth, rgb
    while keep_running:
        # Get a fresh frame
        (depth,_), (rgb,_) = get_depth(), get_video()
        
        # Build a two panel color image
        # d3 = np.dstack((depth,depth,depth)).astype(np.uint8)
        # da = np.hstack((d3,rgb))
        
        results = pose.process(rgb)
        if not results.pose_landmarks:
            continue
        print(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST])

        mp_drawing.draw_landmarks(rgb, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Simple Downsample
        cv2.imshow('both',rgb[:, :, ::-1])
        if cv2.waitKey(10) == 27:
            break
        
def handler(sugnum, frame):
    global keep_running
    keep_running = False

signal.signal(signal.SIGINT, handler)
doloop()
