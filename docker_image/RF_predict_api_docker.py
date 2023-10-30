# flask api to predict iris using random forest model pkl
# expose the api using swagger as UI and documentation, no need for postman
# import libraries
import pickle
from flask import Flask, request
import numpy as np
import pandas as pd
from flasgger import Swagger

# load model from relative path so that it can be deployed on any machine
with open('./model/rf.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# create flask app
app = Flask(__name__)
swagger = Swagger(app)

# create api endpoint and use url to get input for the api
# swagger is used to create UI and documentation for the api, so the """ needs to be followed exactly as below
@app.route('/predict')
def predict_iris():
    """Example endpoint returning a prediction of iris
    ---
    parameters:
      - name: s_length
        in: query
        type: number
        required: true
      - name: s_width
        in: query
        type: number
        required: true
      - name: p_length
        in: query
        type: number
        required: true
      - name: p_width
        in: query
        type: number
        required: true
    """
    # get input from api
    s_length = request.args.get("s_length")
    s_width = request.args.get("s_width")
    p_length = request.args.get("p_length")
    p_width = request.args.get("p_width")
    
    # predict using model
    prediction = model.predict(np.array([[s_length, s_width, p_length, p_width]]))
    return str(prediction)

# create api endpoint and use csv file to get input for the api
@app.route('/predict_file', methods=["POST"])
def predict_iris_file():
    """Example file endpoint returning a prediction list of iris
    ---
    parameters:
      - name: input_file
        in: formData
        type: file
        required: true
    """
    # get input for api
    get_input = request.files.get("input_file") # input_file is the name of the input file for post
    input_data = pd.read_csv(get_input, header=None)
    
    # predict using model
    prediction = model.predict(input_data)
    return str(list(prediction))

# run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
