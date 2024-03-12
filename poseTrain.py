#使用预训练模型和自己的本地数据集进行训练
#一定记得要修改配置文件！（yolov8-pose.yaml / poseTrain.yaml )
from ultralytics import YOLO

# 启动tensorboard可视化辅助训练
# tensorboard --logdir D:\GitHub\ultralytics\runs\pose

# Load a model 加载预训练模型
# model = YOLO('yolov8m-pose.yaml')  # build a new model from YAML 无初始化参数
# model = YOLO('yolov8m-pose.pt')  # load a pretrained model (recommended for training) 使用官方提供的预训练模型做Fine-Tune
# model = YOLO('yolov8m-pose.yaml').load('yolov8m-pose.pt')  # build from YAML and transfer weights 使用自己修改的本地配置文件
model = YOLO(r'D:\GitHub\ultralytics\runs\pose\train39\weights\best.pt')

# Train the model 记得根据自己的设备性能修改超参数
results = model.train(data='poseTrain.yaml', epochs=1,workers = 0,batch = 4)
