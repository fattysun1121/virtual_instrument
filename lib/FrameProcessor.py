# MotionTracking class takes in individual camera frames, processes and calculates
# waist height, hand position, velocity, and acceleration. Draws landmarks on frame
import cv2
import mediapipe as mp
import numpy as np

class FrameProcessor:
    def __init__(self):
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose

        pose = mp_pose.Pose(
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5)

        self.rhand_position = [0, 0, 0]
        self.rhand_velocity = [0, 0, 0]
        self.rhand_accel    = [0, 0, 0]

        self.lhand_position = [0, 0, 0]
        self.lhand_velocity = [0, 0, 0]
        self.lhand_accel    = [0, 0, 0]
        
        self.t1 = 0
        self.t0 = 0

    def draw_landmarks(self, frame):
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        return

    # Retrieve user's waste height
    def get_waist_height(self):
        return

    # Retrieve position, velocity, acceleration
    # Returns 2 3x3 matrices structured as:
    #    Position:     ((px, py, pz),
    #    Velocity:      (vx, vy, vz),
    #    Acceleration:  (ax, ay, az))
    def get_kinematics(self, hand="BOTH"):
        return

    # 
    def process_frame(self, frame):
        results = pose.process(rgb)
        if not results.pose_landmarks:
            return -1
        rhand_position_new = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]
        lhand_position_new = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]

        self.draw_landmarks(frame)


