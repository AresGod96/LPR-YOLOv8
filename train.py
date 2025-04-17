import os

from ultralytics  import YOLO
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

dataset_path = './vn_license_plates/images'
train_path = os.path.join(dataset_path, 'train')
test_path = os.path.join(dataset_path, 'val')
label_path = './vn_license_plates/labels'

train_imgs = [img for img in sorted(os.listdir(train_path)) if img.endswith('.png')]
test_imgs = [img for img in sorted(os.listdir(test_path)) if img.endswith('.png')]
train_labels = []
for img_file in train_imgs:
    label_file = img_file.replace('.png', '.txt')
    label_path_file = os.path.join(label_path, 'train', label_file)
    
    if os.path.exists(label_path_file):
        with open(label_path_file, 'r') as f:
            coords = []
            for line in f.readlines():
                if line.strip():  # Skip empty lines
                    values = [float(x) for x in line.strip().split()]
                    coords.append(values)
            train_labels.append(coords)
    else:
        train_labels.append([])  # Empty list if no label file exists

model = YOLO("./model/yolov8m.pt")
model.info()

model.train(
    data="./vn_license_plates/dataset.yaml",
    epochs=30,
    imgsz=640,
    batch=16,
    name="yolov8m_lp_recognition",
    device='0,1,2,3',
    patience=20
)