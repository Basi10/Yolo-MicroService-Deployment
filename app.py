from flask import Flask, request, jsonify
from script.yolo import YoloModelWrapper
from script.s3_modelstorage import S3ModelStorage
from sqlalchemy import create_engine
import pandas as pd

db_host = 'database-2.c1yyyoas47e9.us-east-1.rds.amazonaws.com'
db_name = 'adludioyolo'
db_user = 'postgres'
db_password = 'admin123'
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}/{db_name}')

app = Flask(__name__)
s3_storage = S3ModelStorage()

#Retrieves the model from S3 bucket
bucket_name = 'adludio-bucket'
local_model_path = 'model/new.pt'
s3_key = 'new.pt'
s3_storage.retrieve_model_to_disk(bucket_name,s3_key,local_model_path)


yolo_wrapper = YoloModelWrapper()

@app.route('/infer', methods=['POST'])
def infer_image():
    # Check if the 'image_url' key exists in the POST request
    if 'image_url' in request.json:
        image_url = request.json['image_url']
        results_df = yolo_wrapper.infer_image(image_url)
        
        # Create a list to store DataFrames for each detected object
        dfs = []
        for index, row in results_df.iterrows():
            # Create a DataFrame for each detected object
            object_df = pd.DataFrame(row).transpose()
            object_df['image_url'] = image_url
            dfs.append(object_df)
        
        # Concatenate DataFrames for each detected object
        final_results_df = pd.concat(dfs, ignore_index=True)
        
        # Rename columns for consistency
        final_results_df = final_results_df.rename(columns={'xmin': 'x_min', 'ymin': 'y_min', 'xmax': 'x_max', 'ymax': 'y_max'})
        
        # Insert into the database
        conn = engine.connect()
        final_results_df.to_sql('detected_objects', conn, if_exists='append', index=False)
        conn.close()
        # Convert to dictionary

        return jsonify(final_results_df.to_dict(orient='records'))
    else:
        return jsonify({'error': 'Please provide an image URL'})

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=int('8000'))
