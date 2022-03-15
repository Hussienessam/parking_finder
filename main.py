import cv2
import cvlib as cv

def model(input_path):
    image = cv2.imread(input_path)
    box, label, count = cv.detect_common_objects(image)
    print("Number of cars in this image are " + str(label.count('car')))
    return label.count('car')