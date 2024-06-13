**1. Trackbar HSV Color Adjustment:**
   - A window named "frame" is created with trackbars to adjust Hue (H), Saturation (S), and Value (V) components of HSV color space.
   - The HSV color values set by the trackbars are used to create an HSV image which is then converted to BGR and displayed in the window.

**2. Camera Index Detection and Color Detection:**
   - Functions are defined to test and find an available camera index.
   - If a camera is found, it is set up with a resolution of 1280x720.
   - In a loop, frames from the camera are read and converted to the HSV color space.
   - The color at the center of the frame is detected and categorized into one of several predefined colors (RED, ORANGE, YELLOW, GREEN, BLUE, VIOLET, WHITE, BLACK, UNDEFINED).
   - A rectangle with the detected color name is displayed on the frame, along with a circle marking the center.
   - The frame is shown in a window until the 'Escape' key is pressed.

**3. Note:**

- "color_recognition.py" works as main.py to run this project


**Video Link of The Project in Action:-** 

https://www.loom.com/share/80dc210d96d143a78ea071f9047d6361?sid=e6a707d1-e66d-437b-9f33-65d60af67551
