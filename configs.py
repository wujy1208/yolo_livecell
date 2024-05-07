model_name = "yolov8-livecell"
model_path = "./ckpts/livecell/weights/best.onnx"
device = "cpu"
batch_size = 1
default_input_size = 640


labels = ['cell']
labels_color = {
    -100: "#949494", 
    0: "#ffffff", 
    1: "#00ff00", 
}


labels_text = {
    0: 'bg', 1: 'cell', 
}


nms_params = {
    "conf_thres": 0.15, #  0.25,  # score_threshold, discards boxes with score < score_threshold
    "iou_thres": 0.45, #  0.7,  # iou_threshold, discards all overlapping boxes with IoU > iou_threshold
    "classes": None, 
    "agnostic": True, # False
    "multi_label": False, 
    "labels": (), 
    "nc": 1,
    "max_det": 300,  # maximum detection
}
