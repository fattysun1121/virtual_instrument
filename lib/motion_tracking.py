# MotionTracking class takes in individual camera frames, processes and calculates
# waist height, hand position, velocity, and acceleration. Draws landmarks on frame
import cv2
import mediapipe as mp
import numpy as np
import time

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
        
        self.t0 = time.time()
        self.dt = 0

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
    def get_kinematics(self):
        a1 = [self.rhand_position, self.rhand_velocity, self.rhand_accel]
        a2 = [self.lhand_position, self.lhand_velocity, self.lhand_accel]
        return

    # Processes frame to calculate hand kinematics
    def process_frame(self, frame):

        # Calculate delta t
        self.dt = time.time() - t0
        results = pose.process(rgb)

        # -1 indicates failure
        if not results.pose_landmarks:
            return -1

        rhand_position_new = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST]
        lhand_position_new = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST]
        
        # Calculate right hand kinematics
        rhand_velocity_new = [0, 0, 0]
        rhand_velocity_new = (rhand_position_new.x - self.rhand_position[0]) / self.dt
        rhand_velocity_new = (rhand_position_new.y - self.rhand_position[1]) / self.dt
        rhand_velocity_new = (rhand_position_new.z - self.rhand_position[2]) / self.dt

        self.rhand_accel[0] = (rhand_velocity_new[0] - self.rhand_velocity[0]) /self.dt
        self.rhand_accel[1] = (rhand_velocity_new[1] - self.rhand_velocity[1]) /self.dt
        self.rhand_accel[2] = (rhand_velocity_new[2] - self.rhand_velocity[2]) /self.dt

        self.rhand_velocity = rhand_velocity_new
        self.rhand_position = rhand_position_new

        # Calculate left hand kinematics
        lhand_velocity_new = [0, 0, 0]
        lhand_velocity_new = (lhand_position_new.x - self.lhand_position[0]) / self.dt
        lhand_velocity_new = (lhand_position_new.y - self.lhand_position[1]) / self.dt
        lhand_velocity_new = (lhand_position_new.z - self.lhand_position[2]) / self.dt

        self.lhand_accel[0] = (lhand_velocity_new[0] - self.lhand_velocity[0]) /self.dt
        self.lhand_accel[1] = (lhand_velocity_new[1] - self.lhand_velocity[1]) /self.dt
        self.lhand_accel[2] = (lhand_velocity_new[2] - self.lhand_velocity[2]) /self.dt

        self.lhand_velocity = lhand_velocity_new
        self.lhand_position = lhand_position_new

        # Draw skeleton on frame after processing
        self.draw_landmarks(frame)
        return 0


