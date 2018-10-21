from flask import Flask, request, send_file
from flask import render_template
import os
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == 'POST':
        file1 = request.files['file1']
        file2 = request.files['file2']
        file1.save('./file1')
        file2.save('./file2')
        return send_file('result.jpg', mimetype='image/jpg')
    else:
        return render_template('index.html')