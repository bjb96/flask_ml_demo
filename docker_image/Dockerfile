# start docker, then cd to the directory where the Dockerfile is located, 
# the folder where the Dockerfile is located should also contain the requirements.txt file, 
# the app.py file, and the model folder with model.pkl file
# then run the command: docker build -t rf_api .

# build base image
FROM continuumio/anaconda3

# copy the content of the local src directory to the working directory in the container
# . means current directory, then space, then /usr/local/bin/ means the working directory in the container
COPY . /usr/local/bin/

# assign port 5000 to the container
EXPOSE 5000

# set the working directory in the container
WORKDIR /usr/local/bin/

# install required packages
RUN pip install -r requirements.txt

# run the command to start app
CMD python RF_predict_api_docker.py