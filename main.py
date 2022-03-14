from imageai.Detection import ObjectDetection
detector = ObjectDetection()
model_path = "./models/yolo-tiny.h5"
input_path = "./input/unknown3.png"
output_path = "./output/newimage.jpg"
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()
detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)
counter = 0
for eachItem in detection:
    if eachItem["name"] == 'car':
        counter = counter + 1
    print(eachItem["name"] , " : ", eachItem["percentage_probability"])
print("num of cars : " , counter)