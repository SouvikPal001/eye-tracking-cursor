import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Initialize Mediapipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Constants for eye landmarks (based on Mediapipe FaceMesh)
LEFT_EYE_LANDMARKS = [33, 160, 158, 133, 153, 144]
RIGHT_EYE_LANDMARKS = [362, 385, 387, 263, 373, 380]

# Screen size
screen_width, screen_height = pyautogui.size()

# Webcam setup
cap = cv2.VideoCapture(0)

# Smooth cursor movement
prev_x, prev_y = screen_width // 2, screen_height // 2
smooth_factor = 0.2  # Adjust for smoother or faster movement

def get_eye_aspect_ratio(eye_points):
    """Calculate Eye Aspect Ratio (EAR) to detect blinks."""
    A = np.linalg.norm(eye_points[1] - eye_points[5])
    B = np.linalg.norm(eye_points[2] - eye_points[4])
    C = np.linalg.norm(eye_points[0] - eye_points[3])
    ear = (A + B) / (2.0 * C)
    return ear

blink_threshold = 0.18  # Adjust this based on testing
blink_counter = 0
blink_frames = 2  # Number of frames for blink confirmation

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            landmarks = face_landmarks.landmark

            # Get average eye position
            left_eye = np.array([[landmarks[i].x * w, landmarks[i].y * h] for i in LEFT_EYE_LANDMARKS])
            right_eye = np.array([[landmarks[i].x * w, landmarks[i].y * h] for i in RIGHT_EYE_LANDMARKS])
            gaze_x = int((left_eye[:, 0].mean() + right_eye[:, 0].mean()) / 2 / w * screen_width)
            gaze_y = int((left_eye[:, 1].mean() + right_eye[:, 1].mean()) / 2 / h * screen_height)

            # Smooth cursor movement
            prev_x = int(prev_x + (gaze_x - prev_x) * smooth_factor)
            prev_y = int(prev_y + (gaze_y - prev_y) * smooth_factor)
            pyautogui.moveTo(prev_x, prev_y, duration=0.05)

            # Detect blink
            left_ear = get_eye_aspect_ratio(left_eye)
            right_ear = get_eye_aspect_ratio(right_eye)
            ear = (left_ear + right_ear) / 2

            if ear < blink_threshold:
                blink_counter += 1
            else:
                if 1 <= blink_counter <= blink_frames:
                    pyautogui.click()
                blink_counter = 0

    cv2.imshow("Eye Tracking Cursor", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
