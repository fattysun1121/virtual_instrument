# import necessary packages
import pyrealsense2.pyrealsense2 as rs
import cv2
import mediapipe as mp
import numpy as np

# initialize Pose estimator
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

pipe = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
pipe.start(config)

while True:
    frames = pipe.wait_for_frames()
    color = frames.get_color_frame()
    width = color.get_width()
    height = color.get_height()
    color_array = np.asanyarray(color.get_data())
    

    # process the RGB frame to get the result
    results = pose.process(color_array)

    if not results.pose_landmarks: continue

    print(
        f'Left Wrist coordinates: ('
        f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].x * width}, '
        f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y * height})'
    )

    print(
        f'Right Wrist coordinates: ('
        f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x * width}, '
        f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y * height})'
    )
    # draw detected skeleton on the frame
    mp_drawing.draw_landmarks(color_array, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    
    # show the final output
    cv2.imshow('Output', color_array)
    
    if cv2.waitKey(1) == ord('q'):
        break

pipe.stop()
cv2.destroyAllWindows()