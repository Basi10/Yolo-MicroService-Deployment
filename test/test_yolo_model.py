import os
import torch
import pandas as pd



def test_yolo_model_detection():
    image_url = "https://cdn.thewirecutter.com/wp-content/media/2023/09/budgetandroidphones-2048px-6942.jpg?auto=webp&quality=75&crop=1.91:1&width=1200"

    # Define the expected detections for cell phones
    expected_detections = [
        {
            "x_min": 775.099609375, "y_min": 87.14508056640625, "x_max": 1026.26513671875, "y_max": 583.906494140625,
            "confidence": 0.7095,  # Minimum confidence threshold for detection
            "class": 67,
            "name": "cell phone",
            
            
        },
        {
            "x_min": 170.36526489257812, "y_min": 91.25164794921875, "x_max": 410.15478515625, "y_max": 589.7283325195312,
            "confidence": 0.6131,  # Minimum confidence threshold for detection
            "class": 67,
            "name": "cell phone",
           
            
        },
        {
             "x_min": 469.22998046875,
            "y_min": 81.4748764038086,
            "x_max": 717.1421508789062,
            "y_max": 573.086669921875,
            "confidence": 0.5221,  # Minimum confidence threshold for detection
            "class": 67,
            "name": "cell phone",
            
        }
    ]
    expected_df = pd.DataFrame(expected_detections)

    # Load the YOLO model
    abs_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../model/new.pt')
    model = torch.hub.load('ultralytics/yolov5', 'custom', abs_path)
    
    # Perform detection
    result = model(image_url).pandas().xyxy[0]
    final_results_df = result.rename(columns={'xmin': 'x_min', 'ymin': 'y_min', 'xmax': 'x_max', 'ymax': 'y_max'})
    final_results_df['confidence'] = final_results_df['confidence'].round(4)
    # Compare DataFrames
    assert expected_df.equals(final_results_df), "Expected and actual detections do not match"
    

if __name__ == "__main__":
    pytest.main()
