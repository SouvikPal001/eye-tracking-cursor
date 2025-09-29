# 👁️ Eye Tracking Cursor

An AI-powered Python project that lets you **control the mouse cursor using your eyes**.  
It uses dlib's 68-point facial landmark detector to locate eyes and detect blinks, maps eye movement to screen coordinates, and uses a blink as a left-click.

---

## ✨ Features
- Real-time eye tracking using your webcam  
- Cursor control by moving your eyes (along with your head for now actually)
- Left-click action triggered by an intentional blink  
- Smooth cursor movement for a better user experience

---

## 🛠️ Technologies Used
- Python 3  
- dlib (facial landmark detection)  
- OpenCV (video capture & image processing)  
- pyautogui (cursor control & clicking)  
- imutils (utility functions)

---

## 📂 Project Structure
    ├── main.py                                # Main script for eye tracking and cursor control
    ├── shape_predictor_68_face_landmarks.dat  # Pre-trained dlib model (large file, tracked with Git LFS)
    ├── .gitignore

---

## 🚀 Setup & Usage

1. Clone the repository:
    git clone https://github.com/SouvikPal001/eye-tracking-cursor.git
    cd eye-tracking-cursor

2. Install dependencies:
    pip install -r requirements.txt

   If `requirements.txt` is not present, install manually:
    pip install opencv-python dlib imutils pyautogui

3. Run the project:
    python main.py

Your webcam will open and the program will begin tracking eye movement. Move your eyes to move the cursor; blink to perform a left-click.

---

## ⚠️ Important Notes
- The `shape_predictor_68_face_landmarks.dat` file is large (~95 MB). It is tracked using **Git LFS** in this repository. If you clone the repo, make sure Git LFS is installed on your system:
    https://git-lfs.github.com/

---

## 🎯 Future Improvements
- Add right-click (e.g., double-blink) and context-menu actions  
- Implement drag-and-drop via prolonged eye-gaze or blink-and-hold  
- Improve accuracy and robustness with better smoothing, calibration, and ML models  
- Add configuration options for sensitivity, smoothing, and screen calibration

---

## 📌 Work in Progress
This project performs the **basic tasks** (cursor movement and left-click via blink), but it is still a **work in progress** and requires further improvements for stability, accuracy, and usability.
