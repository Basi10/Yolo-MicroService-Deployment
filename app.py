from flask import Flask, request, jsonify
from script.yolo import YoloModelWrapper

app = Flask(__name__)
yolo_wrapper = YoloModelWrapper()



@app.route('/infer', methods=['POST'])
def infer_image():
    # Check if the 'image_url' key exists in the POST request
    if 'image_url' in request.json:
        image_url = request.json['image_url']
        results_df = yolo_wrapper.infer_image(image_url)
        return jsonify(results_df.to_dict(orient='records'))
    else:
        return jsonify({'error': 'Please provide an image URL'})

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=int('8000'))
