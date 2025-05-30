from ultralytics import YOLO
model = YOLO(model='yolo11n.pt')  # load a pretrained model (recommended for training)
results = model(task='detect', source='./test.jpg', save=True)  # predict on an image
