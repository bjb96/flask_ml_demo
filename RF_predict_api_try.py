# flask api to predict iris using random forest model pkl
# import libraries
import pickle
from flask import Flask, request
import numpy as np
import pandas as pd

# load model from relative path so that it can be deployed on any machine
with open('./model/rf.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# create flask app
app = Flask(__name__)

# create api endpoint and use url to get input for the api
@app.route('/predict')
def predict_iris():
    """Example endpoint returning a prediction of iris
    ---
    parameters:
    parameters:
      - {"name": "s_length", "type": "real", "required": true, "in": "query"}
      - {"name": "s_width", "type": "real", "required": true, "in": "query"}
      - {"name": "p_length", "type": "real", "required": true, "in": "query"}
      - {"name": "p_width", "type": "real", "required": true, "in": "query"}
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
    """Example file endpoint returning a prediction of iris
    ---
    parameters:
      - {"name": "input", "type": "csv", "required": true, "in": "formData"}
    """
    # get input for api
    get_input = request.files.get("input_file") # input_file is the name of the input file for post
    input_data = pd.read_csv(get_input, header=None)
    
    # predict using model
    prediction = model.predict(input_data)
    return str(list(prediction))

# run app
if __name__ == '__main__':
    app.run()
