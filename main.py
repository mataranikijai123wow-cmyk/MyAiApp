import flet as ft
import cv2
import mediapipe as mp
import numpy as np

def main(page: ft.Page):
    # Setup the mobile app screen
    page.title = "AI Animator Base"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.scroll = "adaptive"

    # 1. Test that Numpy works
    test_array = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # 2. Test that OpenCV (cv2) works
    # We draw a line on the invisible numpy image to prove cv2 is active
    cv2.line(test_array, (0, 0), (100, 100), (255, 0, 0), 5)
    
    # 3. Test that MediaPipe works
    mp_face_detection = mp.solutions.face_detection
    face_detector = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

    # If the app reaches this point without crashing, all heavy libraries are successfully installed!
    
    # Create the UI to show success
    status_icon = ft.Icon(name=ft.icons.CHECK_CIRCLE, color=ft.colors.GREEN_400, size=80)
    status_text = ft.Text(
        "Success! AI Brains Loaded.", 
        size=24, 
        weight=ft.FontWeight.BOLD,
        color=ft.colors.WHITE
    )
    details_text = ft.Text(
        "OpenCV, MediaPipe, and Numpy are successfully running on your Android device.",
        text_align=ft.TextAlign.CENTER,
        color=ft.colors.WHITE70
    )

    # Add elements to the screen
    page.add(
        status_icon,
        status_text,
        details_text
    )

# Run the app
ft.app(target=main)
