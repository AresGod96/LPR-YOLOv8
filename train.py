import os

from ultralytics  import YOLO
import numpy as np
import matplotlib.pyplot as plt

dataset_path = './vn_license_plates/images'
train_path = os.path.join(dataset_path, 'train')
test_path = os.path.join(dataset_path, 'val')

model = YOLO("./model/yolov8m.pt")
model.info()

model.train(
    data="./vn_license_plates/dataset.yaml",
    epochs=30,
    imgsz=640,
    batch=64,
    name="yolov8m_lp_recognition",
    device='0,1',
    patience=20
)