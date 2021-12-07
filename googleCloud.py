"""
import os

import google.cloud 

from google.cloud import storage

#import flask

from flask import Flask, render_template, request, redirect, jsonify, make_response


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'flask-api-334318-5e4fb13d61bd.json'

storage_client = storage.Client()

#bucket_name = "my_kidney_file_bucket"

#bucket = storage_client.create_bucket(bucket_name)

dir(storage_client)

bucket_name = 'kidney_cloud_test_file_bucket'
bucket = storage_client.bucket(bucket_name)
#bucket.location = 'US'
bucket = storage_client.create_bucket(bucket)

vars(bucket)

my_bucket = storage_client.get_bucket('kidney_cloud_test_file_bucket')

def upload_to_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as weirdCase:
        print(weirdCase)
        return False

file = request.files["inpFile"]
file_path = os.path.abspath(file)

upload_to_bucket('dataFile', os.path.join(file_path, file.filename), 'kidney_cloud_test_file_bucket')



#from flask import Flask, render_template, request, redirect, jsonify, make_response

"""