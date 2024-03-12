#使用本地训练好的模型进行推理
from ultralytics import YOLO

#加载自己的模型
model = YOLO(r'D:\GitHub\ultralytics\runs\pose\train39\weights\best.pt')  # load a custom model

#开始验证或者推理,此处可以使用单个图片或者文件夹
model.predict(r'C:\Users\John\Desktop\ultralytics-main\ultralytics-main\datasets\RM-L\images\val', save=True, show = True, conf=0.5)

