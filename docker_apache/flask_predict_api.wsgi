#! /usr/bin/python

import sys
sys.path.insert(0, "/var/www/RF_predict_api_docker") # This is the path to your application's code
sys.path.insert(0,'/opt/conda/lib/python3.6/site-packages') # This is the path to your python site-packages
sys.path.insert(0, "/opt/conda/bin/") # This is the path to your python site-packages

import os
os.environ['PYTHONPATH'] = '/opt/conda/bin/python' # This is the path to your python site-packages

from RF_predict_api_docker import app as application # This is your application object