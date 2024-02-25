import cv2
import numpy as np
import pyautogui

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('screen_record.mp4', fourcc, 20.0, (1920, 1080))

while True:
    # Take screenshot using pyautogui
    img = pyautogui.screenshot()

    # Convert the screenshot to an array and then to BGR
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Write the frame to the output video file
    out.write(frame)

    # Display the recording in real-time (optional)
    cv2.imshow('Screen Recording', frame)
    
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the VideoWriter and destroy OpenCV windows
out.release()
cv2.destroyAllWindows()
