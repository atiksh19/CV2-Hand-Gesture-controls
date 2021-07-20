# CV2-Hand-Gesture-controls
OpenCV and mediapipe for hand gesture control. perform basic tasks such as play/pause, copy/paste, switch tabs, using hand gestures...
# Project
OpenCV is a very useful python library that help process image files and access the webcam. Using mediapipe, the webcam stream is processed, and the hand is found. The handTracker.py file(by Murtaza's workshop with a few changes by me) consists of the hand detection and tracking. The streaming, gesture detection, and the functionality is in the main.py file. THIS CODE ONLY WORKS ON WINDOWS.
# How it Works
The handTracker.py file returns the hand position and landmarks. It consists of 20 landmarks, for different parts of your hand. Then using the landmarks and a fairly simple algorithm, the code checks if each finger is open or closed. After that the gestures are detected and using the pynput library, a keyboard shortcut is used to execute the task. Each task can be performed only once and to repeat a task a reset gesture is used. This is done in order to prevent the code from executing the same task multiple times.
# Functionality
1. Open all fingers to reset
2. Play
3. Pause
4. Copy selected
5. Paste
6. Next tab
7. Previous tab
8. Minimize window
9. Maximize window
10. Move cursor
11. Click
# Demo Video
[![CV2-Hand-Gesture-controls](https://img.youtube.com/vi/O2JaNA2f2qk/0.jpg)](https://www.youtube.com/watch?v=O2JaNA2f2qk)
