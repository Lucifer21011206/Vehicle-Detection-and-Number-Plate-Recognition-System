**-----   Vehicle Detection and Number Plate Recognition System   -----** 

This Project showcases computer vision using OpenCV, number plate recognition using Tesseract OCR, and web development using Flask. The system is capable of detecting vehicles from a a pre-recorded video  (or a live video stream), extracting the vehicle's number plates, counting the number of vehicles, and displaying real-time data on a web interface.

Project Overview

The Vehicle Detection and Number Plate Recognition System is a multi-functional application designed to detect moving vehicles from a video stream, recognize their number plates, and count them. It leverages OpenCV for object detection, Tesseract for Optical Character Recognition (OCR), and Flask to present the data on a web interface.

The system works in the following stages:

    Video Stream Capture: Captures real-time video from a camera or a pre-recorded file.
    Vehicle Detection: Uses a pre-trained model (Haar Cascade) to detect vehicles in the stream and draw bounding boxes around them.
    Number Plate Recognition: Extracts the number plate region from the detected vehicle and uses Tesseract OCR to read the text.
    Vehicle Counting: Keeps track of the total number of vehicles detected in the video stream.
    Web Interface: Displays the vehicle count and recognized number plates on a simple web interface using Flask.

Features

    Real-time Vehicle Detection: Detects moving vehicles in real-time or from a pre-recorded video.
    Number Plate Recognition: Uses Tesseract OCR to read and display vehicle number plates.
    Vehicle Counting: Maintains a count of the total number of vehicles detected in the video.
    Flask Web Interface: Presents real-time vehicle data (count and plates) on a web interface.

File Structure:



project/
├── app.py          # Flask application for web interface
├── detection.py    # OpenCV-based vehicle detection
├── ocr.py          # Number plate reading using Tesseract
├── vehicle_data.py # Global storage for vehicle count and plates
├── templates/
│   └── index.html  # Web page template


Key Components

    app.py: Initializes the Flask app and handles routing. It starts a background thread for video capture and detection.
    detection.py: Uses Haar Cascade Classifier from OpenCV to detect vehicles in the video stream and extracts the number plate region.
    ocr.py: Responsible for reading the number plate using Tesseract OCR.
    vehicle_data.py: A global dictionary that stores vehicle count and recognized plates.
    index.html: The frontend HTML template for displaying the vehicle data in the browser.



How It Works:

  Video Stream

    The system captures video frames from a video file (or a camera) and processes each frame in real-time.

  Vehicle Detection

    OpenCV’s Haar Cascade Classifier is used to detect vehicles in the video frame. Bounding boxes are drawn around detected vehicles.

  Number Plate Recognition

    After detecting a vehicle, the system extracts the region of interest (ROI) corresponding to the vehicle’s number plate and processes it with Tesseract OCR to retrieve the text.

  Vehicle Counting

    The number of detected vehicles is continuously tracked and displayed on the web interface.

  Web Interface

    Flask serves a real-time display of the vehicle count and number plates through the / route, using index.html to show the data in a user-friendly format.


Future Enhancements

  Here are some potential improvements and additional features that could be added to the system:

    Improved Detection: Implement a more robust vehicle detection model such as YOLO or SSD to enhance accuracy and performance.
    Database Integration: Store the recognized number plates in a database for later retrieval and analysis.
    Multi-camera Support: Extend the system to support multiple video streams simultaneously.
    Better Error Handling: Implement more sophisticated error handling for cases where number plates are unclear or unreadable.

  Acknowledgments

    OpenCV for providing powerful tools for computer vision tasks.
    Tesseract for its robust OCR capabilities.
    Flask for simplifying the creation of the web interface.
