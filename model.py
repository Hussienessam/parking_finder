from imageai.Detection import ObjectDetection
import os

entries = os.listdir('input/')
detector = ObjectDetection()
for entry in entries:
    input_path = "./input/" + entry
    model_path = "./models/yolo-tiny.h5"
    output_path = "./output/" + entry
    detector.setModelTypeAsTinyYOLOv3()
    detector.setModelPath(model_path)
    detector.loadModel()
    detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)
    counter = 0
    for eachItem in detection:
        if eachItem["name"] == 'car':
            counter = counter + 1
    print(entry + " num of cars : " , counter)
