import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def read_number_plate(roi):
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    return pytesseract.image_to_string(gray, config='--psm 8').strip()
