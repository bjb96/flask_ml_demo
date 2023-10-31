# based image from continuumio/anaconda3
FROM continuumio/anaconda3

# port 8000 for mod_wsgi
EXPOSE 8000

# install apache2 and mod_wsgi
RUN apt-get update && apt-get install -y apache2 \
    apache2-dev \   
    vim \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*

# define environment variable 
WORKDIR /var/www/RF_predict_api_docker/

# copy files
COPY ./flask_predict_api.wsgi /var/www/RF_predict_api_docker/flask_predict_api.wsgi
COPY ./flask /var/www/RF_predict_api_docker/

# install python packages
RUN pip install -r requirements.txt

# install mod_wsgi
RUN /opt/conda/bin/mod_wsgi-express install-module
RUN mod_wsgi-express setup-server flask_predict_api.wsgi --port=8000 \
    --user www-data --group www-data \
    --server-root=/etc/mod_wsgi-express-80

# run apache2
CMD /etc/mod_wsgi-express-80/apachectl start -D FOREGROUND
