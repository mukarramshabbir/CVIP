import cv2

def apply_filter(frame, filter_type):
    if filter_type == 'GRAY':
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif filter_type == 'BLUR':
        return cv2.GaussianBlur(frame, (15, 15), 0)
    elif filter_type == 'CANNY':
        return cv2.Canny(frame, 100, 200)
    else:
        return frame

def main():
    video_path = 'Paisa.mp4'  # Update with your video file path
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    filter_type = None

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if filter_type:
            frame = apply_filter(frame, filter_type)

        cv2.imshow('Video Player', frame)

        key = cv2.waitKey(30)

        if key == 27:  # ESC key to exit
            break
        elif key == ord('f'):  # Forward 10 seconds
            cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) + cap.get(cv2.CAP_PROP_FPS) * 10)
        elif key == ord('b'):  # Backward 10 seconds
            cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) - cap.get(cv2.CAP_PROP_FPS) * 10)
        elif key == ord('g'):  # Apply GRAY filter
            filter_type = 'GRAY'
        elif key == ord('c'):  # Apply CANNY filter
            filter_type = 'CANNY'
        elif key == ord('d'):  # Apply BLUR filter
            filter_type = 'BLUR'
        elif key == ord('r'):  # Reset filter
            filter_type = None

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
