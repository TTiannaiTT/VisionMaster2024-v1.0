# VisionMaster2024 v1.0
Here is *part* of our vision code for our RoboMaster 2024 competition.  
We rank top 16 in the RoboMaster University Championship, Final Tournament 2024. It's really a breakthrough for our 3SE team and our school.🎉🎉🎉 
## Vision Model
We choose yolov8-pose as our base model for these tasks. It features low latency, light weight and competitive performance under this condition.  
This season we only build a simple fine-tuned version of the YOLOv8 model for Robomaster competition. (Maybe with just a little specific design...)  
The performance and robustness of the model is really a surprise! Please refer to the YOLOv8 official reposity for more information: [ultralytics](https://github.com/ultralytics/ultralytics)

![image](https://github.com/user-attachments/assets/ba8ee494-0a12-4592-aada-f9b982aa9b8f)

## Inference Acceleration
Hardware: Nvidia Jetson Orin NX (16GB)  
Software: TensorRT(C++ backend) + multiple model parallel inference  

## Notice  
Now only part of the vision task code is included.    
Besides the detection and pose estimation, the acceleration of the inference of this network is also important. I will also upload that later.
