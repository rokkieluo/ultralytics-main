# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

import onnx
from onnxsim import simplify

# 加载预定义的 ONNX 模型
model = onnx.load("yolov11n.onnx")

# 简化模型
model_simp, check = simplify(model)

# 确保简化后的模型有效
assert check, "Simplified ONNX model could not be validated"

# 保存简化后的模型
onnx.save(model_simp, "yolov11n-sim.onnx")
