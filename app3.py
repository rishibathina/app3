import os

import google.cloud 

import glob

from google.cloud import storage
#from google.cloud import storage

#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'flask-api-334318-5e4fb13d61bd.json'
 
from flask import Flask, render_template, request, redirect, jsonify, make_response


#storage_client = storage.Client()

app = Flask(__name__)

#@app.route("/")
#def index():
#    return "Hello World!"

if __name__ == "__main__":
    app.run(host="localhost", port=7888, debug=False)

#file = {}

@app.route("/upload", methods=["GET","POST"])
def upload_file():
    if request.method=="POST":
        #global file 
        file = request.files["inpFile"]
        #theFile = file
        file.save(os.path.join("uploads", file.filename))
        return render_template("uploadFile.html", message="success")
    return render_template("uploadFile.html", message="Upload")

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'flask-api-334318-5e4fb13d61bd.json'
#print("I am after upload_file")
list_of_files = glob.glob('./uploads/*') 
#print(list_of_files)
latest_file = max(list_of_files, key=os.path.getctime)
#print(latest_file)

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


upload_to_bucket('dataFile', latest_file, 'kidney_cloud_test_file_bucket')



#from flask import Flask, render_template, request, redirect, jsonify, make_response
