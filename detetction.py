import cv2
from ocr import read_number_plate
from vehicle_data import vehicle_data

vehicle_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_car.xml')


def detect_vehicles(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    vehicles = vehicle_cascade.detectMultiScale(gray, 1.1, 2)
    for (x, y, w, h) in vehicles:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    return frame, vehicles


def update_vehicle_data():
    cap = cv2.VideoCapture("cars.mp4")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame, vehicles = detect_vehicles(frame)
        vehicle_data["count"] += len(vehicles)
        if vehicles:
            x, y, w, h = vehicles[0]
            roi = frame[y:y+h, x:x+w]
            plate = read_number_plate(roi)
            if plate:
                vehicle_data["plates"].append(plate)
        cv2.imshow('Video Stream', frame)
        if cv2.waitKey(1) & 0xFF == ord('esc'):
            break
    cap.release()
    cv2.destroyAllWindows()
