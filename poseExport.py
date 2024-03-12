#本地模型权重的导出
import torch
from ultralytics import YOLO
from onnxsim import simplify
import onnx

#加载自己的模型
# model = YOLO(r'D:\GitHub\ultralytics\runs\pose\train39\weights\best.pt')  # load a custom model
model = YOLO('yolov8s-pose.pt')  # load a pretrained model (recommended for training) 使用官方提供的预训练模型做Fine-Tune

model = model.cuda()

# print(model)

#导出不同格式的模型文件
model.export(format='onnx')
# onnx_model = onnx.load(r'D:\GitHub\ultralytics\runs\pose\train39\weights\best.onnx') # load onnx model
# # model_simp, check = simplify(onnx_model)
#
# # assert check, "Simplified ONNX model could not be validated"
# # onnx.save(model_simp, r'D:\GitHub\ultralytics\runs\pose\train39\weights\best_sim.onnx')
#
# print(onnx_model)
# print('finished exporting onnx')
# graph = onnx_model.graph
# print(graph.output) # 看onnx模型的数据类型和结构信息



