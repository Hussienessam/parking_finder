import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
import os

entries = os.listdir('input/')
outpath = './output/'

if not os.path.exists(outpath):
    os.makedirs(outpath)

for entry in entries:
    input_path = "./input/" + entry
    image = cv2.imread(input_path)

    box, label, count = cv.detect_common_objects(image)
    output = draw_bbox(image, box, label, count)
    plt.imshow(output)

    print("Number of cars in " + entry + " are " + str(label.count('car')))
    plt.savefig(outpath + entry)