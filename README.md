# flask_ml_demo
example to build a ML model and expose it as API endpoint

1. train random forest model and save as pkl
2. expose the model as api endpoint in 2 ways: get and post
- the get method will expose the model input in URL
- the post method will ask user to provide a input file (csv format with 4 columns as model inputs as a batch)
3. expose the model as api contained in a docker image that can be deployed anywhere
- the process and all dependent files are saved in the docker_image folder