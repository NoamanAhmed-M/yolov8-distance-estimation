Real-Time Object Distance Estimation using YOLOv8 and OpenCV

This project uses [YOLOv8](https://github.com/ultralytics/ultralytics) and OpenCV to detect objects (specifically people) in real-time and estimate their distance from the camera using basic geometry and bounding box size.

 Note: This system does **not** calculate a person’s actual height. Instead, it assumes an average height (e.g., 1.7m) to estimate distance.


- Real-time object detection using YOLOv8
- Webcam feed with bounding boxes and distance overlay
- Adjustable focal length for camera calibration
- Modular and easy to extend

---

 Requirements

- Python 3.8+
- OpenCV
- NumPy
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)

### Install dependencies

```bash
pip install opencv-python numpy ultralytics

 How It Works
Distance estimation formula:
distance = (real_object_height * focal_length) / object_pixel_height
real_object_height: Assumed to be 1.7 meters for people

focal_length: Must be calibrated for your specific camera

object_pixel_height: Height of bounding box in the image

Camera Calibration Required!
You must adjust the FOCAL_LENGTH variable to match your camera. A default value (e.g., 615) may give inaccurate results if not calibrated.

How to calibrate:
Place an object (like a person or bottle) at a known distance (e.g. 2 meters).

Measure its bounding box height in pixels (e.g. 480).

Use this formula to calculate your focal length:

focal_length = (object_pixel_height * known_distance) / real_object_height
Update FOCAL_LENGTH in your code accordingly.
