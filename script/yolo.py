import os
import torch
import pandas as pd

class YoloModelWrapper:
    def __init__(self):
        abs_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../model/new.pt')
        self.model = torch.hub.load('ultralytics/yolov5', 'custom',abs_path)

    def infer_image(self, img):
        """
        Method to perform inference on an image using the YOLO model.

        Args:
            img: Can be a URL, path to a local image file, or the image itself (PIL, OpenCV, numpy).

        Returns:
            Pandas DataFrame containing inference results.
        """
        # Run inference
        results = self.model(img)

        # Return results as a Pandas DataFrame
        return results.pandas().xyxy[0]


