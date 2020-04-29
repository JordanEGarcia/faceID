import numpy
import cv2
import os
from flask import Flask, flash, request, redirect, url_for

UPLOAD_FOLDER = '/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

#initialize
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#home page
@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method=='POST':
        return "<h1>POST</h1>"
    if request.method=='GET':
        return "<h1>GET</h1>"

if __name__ == "__main__":
    app.run(debug=True)
