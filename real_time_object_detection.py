# installation packages
# virtual enviroment would be better option here
# pip install tensorflow==2.4.0
# pip install keras==2.4.3
# pip install numpy==1.19.3
# pip install pillow==7.0.0
# pip install scipy==1.4.1
# pip install h5py==2.10.0
# pip install matplotlib==3.3.2
# pip install opencv-python
# pip install keras-resnet==0.2.0
# pip install imageai --upgrade
# 
from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.1.0.h5"))
detector.loadModel()
detections = detector.detectObjectFromImage(input_image = os.path.join(execution_path,
	"image.jpg"), output_image_path = os.path.join(execution_path, "imagenew.jpg"))

for eachObject in detections:
	print(eachObject["name"], ":", eachObject["percentage_probability"])

# Download RetinaNet model file:

# just browse on the web and you will find it and
# place it in your folder where code is written


