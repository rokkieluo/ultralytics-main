# RK3588的yolo11模型转换(pt->onnx)

本教程适用于6个输出头的onnx目标检测模型，如需9个输出头，请参考rk官方的示例：[airockchip/ultralytics_yolo11](https://github.com/airockchip/ultralytics_yolo11)

第一步：获取本仓库代码

```bash
git clone https://github.com/rokkieluo/ultralytics-main.git
```

第二步：更改model.py

该文件位于ultralytics-main/ultralytics/engine/model.py

找到第313行，将导出路径设置为你自己的导出路径和导出文件名

```python
torch.onnx.export(self.model, dummy_input,"C:/Users/15346/Desktop/yolov5/yolo11/ultralytics-main/yolov11n.onnx", verbose=False, input_names=input_names, output_names=output_names, opset_version=11)
```

第三步：更改export.py

```python
from ultralytics import YOLO
model = YOLO(model='yolo11n.pt')  # load a pretrained model (recommended for training)
results = model(task='detect', source='./test.jpg', save=True)  # predict on an image
```

将代码中的

```python
model = YOLO(model='yolo11n.pt')
```

改为你自己的模型路径

第四步：运行

```bash
python export.py
```

运行可能会报错，但是不影响onnx模型生成，只要能生成onnx模型，不必理会报错

第五步：简化onnx模型

打开simplify_onnx.py，更改模型路径

```python
model = onnx.load('yolov11n.onnx') #改为你自己刚刚导出的onnx模型路径
```

更改导出路径

```python
onnx.save(model_simp, 'yolov11n-sim.onnx') #改为你自己的导出模型名
```

第六步：运行

```bash
python simplify_onnx.py
```

至此就可以得到适用于6个输出头的onnx模型，可在netron中自行检查