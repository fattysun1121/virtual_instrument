# MotionTracking class takes in individual camera frames, processes and calculates
# waist height, hand position, velocity, and acceleration. Draws landmarks on frame
import cv2
import mediapipe as mp
import numpy as np
import time

class FrameProcessor:
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose

        self.pose = self.mp_pose.Pose(
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5)

        self.rhand_position = [0, 0, 0]
        self.rhand_velocity = [0, 0, 0]
        self.rhand_accel    = [0, 0, 0]

        self.lhand_position = [0, 0, 0]
        self.lhand_velocity = [0, 0, 0]
        self.lhand_accel    = [0, 0, 0]
        
        self.t0 = 0

    def draw_landmarks(self, frame, results):
        self.mp_drawing.draw_landmarks(frame, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)

    # Retrieve position, velocity, acceleration
    # Returns 2 3x3 matrices structured as:
    #    Position:     ((px, py, pz),
    #    Velocity:      (vx, vy, vz),
    #    Acceleration:  (ax, ay, az))
    def get_kinematics(self, hand="BOTH"):
        a1 = [self.lhand_position, self.lhand_velocity, self.lhand_accel]
        a2 = [self.rhand_position, self.rhand_velocity, self.rhand_accel]
        return a1, a2

    # Processes camera frames
    def process_frame(self, frame):

        # Calculate delta t
        t1 = time.time()
        dt = t1 - self.t0
        self.t0 = t1
        results = self.pose.process(frame)

        # -1 indicates failure
        if not results.pose_landmarks:
            return -1

        # Get new positions of right hand and left hand
        rhand_new_px = results.pose_landmarks.landmark[self.mp_pose.PoseLandmark.RIGHT_WRIST].x
        rhand_new_py = results.pose_landmarks.landmark[self.mp_pose.PoseLandmark.RIGHT_WRIST].y
        rhand_new_pz = results.pose_landmarks.landmark[self.mp_pose.PoseLandmark.RIGHT_WRIST].z

        lhand_new_px = results.pose_landmarks.landmark[self.mp_pose.PoseLandmark.LEFT_WRIST].x
        lhand_new_py = results.pose_landmarks.landmark[self.mp_pose.PoseLandmark.LEFT_WRIST].y
        lhand_new_pz = results.pose_landmarks.landmark[self.mp_pose.PoseLandmark.LEFT_WRIST].z


        # Calculate right hand kinematics
        rhand_velocity_new = [0, 0, 0]
        rhand_velocity_new[0] = (rhand_new_px - self.rhand_position[0]) / dt
        rhand_velocity_new[1] = (rhand_new_py - self.rhand_position[1]) / dt
        rhand_velocity_new[2] = (rhand_new_pz - self.rhand_position[2]) / dt

        self.rhand_accel[0] = (rhand_velocity_new[0] - self.rhand_velocity[0]) /dt
        self.rhand_accel[1] = (rhand_velocity_new[1] - self.rhand_velocity[1]) /dt
        self.rhand_accel[2] = (rhand_velocity_new[2] - self.rhand_velocity[2]) /dt

        self.rhand_velocity = rhand_velocity_new
        self.rhand_position = [rhand_new_px, rhand_new_py, rhand_new_pz]

        # Calculate left hand kinematics
        lhand_velocity_new = [0, 0, 0]
        lhand_velocity_new[0] = (lhand_new_px - self.lhand_position[0]) / dt
        lhand_velocity_new[1] = (lhand_new_py - self.lhand_position[1]) / dt
        lhand_velocity_new[2] = (lhand_new_pz - self.lhand_position[2]) / dt

        self.lhand_accel[0] = (lhand_velocity_new[0] - self.lhand_velocity[0]) / dt
        self.lhand_accel[1] = (lhand_velocity_new[1] - self.lhand_velocity[1]) / dt
        self.lhand_accel[2] = (lhand_velocity_new[2] - self.lhand_velocity[2]) / dt

        self.lhand_velocity = lhand_velocity_new
        self.lhand_position = [lhand_new_px, lhand_new_py, lhand_new_pz]

        # Draw skeleton on frame after processing
        self.draw_landmarks(frame, results)

        return 0
