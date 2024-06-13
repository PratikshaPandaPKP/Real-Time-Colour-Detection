import cv2


def test_camera(index):
    cap = cv2.VideoCapture(index)
    return cap.isOpened()


def find_camera_index():
    return next((i for i in range(10) if test_camera(i)), None)


camera_index = find_camera_index()
if camera_index is None:
    print("No camera found.")
    exit(1)
else:
    print("Using camera with index:", camera_index)

cap = cv2.VideoCapture(camera_index)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

try:
    while True:
        ret, frame = cap.read()
        if not ret or frame is None:
            print("Error: Failed to receive frame.")
            break

        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        height, width, _ = frame.shape
        cx, cy = width // 2, height // 2

        pixel_center = hsv_frame[cy, cx]
        hue_value = pixel_center[0]

        color = "Undefined"
        if 0 <= hue_value < 5 or 160 <= hue_value <= 179:
            color = "RED"
        elif 5 <= hue_value < 22:
            color = "ORANGE"
        elif 22 <= hue_value < 33:
            color = "YELLOW"
        elif 33 <= hue_value < 78:
            color = "GREEN"
        elif 78 <= hue_value < 131:
            color = "BLUE"
        elif 131 <= hue_value < 170:
            color = "VIOLET"
        elif hue_value < 10 or hue_value > 160:
            if 20 < pixel_center[1] < 235 and 20 < pixel_center[2] < 235:
                color = "WHITE"
            elif pixel_center[1] < 20 and pixel_center[2] < 20:
                color = "BLACK"
            else:
                color = "UNDEFINED"

        b, g, r = map(int, frame[cy, cx])
        cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
        cv2.putText(frame, color, (cx - 200, 100), 0, 3, (b, g, r), 5)

        # Increase the radius of the circle
        cv2.circle(frame, (cx, cy), 15, (25, 25, 25), 3)

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

except KeyboardInterrupt:
    pass

cap.release()
cv2.destroyAllWindows()