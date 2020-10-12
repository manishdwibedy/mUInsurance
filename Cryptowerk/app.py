from flask import Flask, jsonify, request
import hashlib
import requests
from lib import getHash, register, verify, allowed_file
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'C:\\Development\\Personal\\mU-Insurance\\'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    status = {
        'status': "Running",
        "error": False
    }
    return jsonify(status)

@app.route('/hashText')
def hashText(te):
    hash = getHash("C:\\Development\\Personal\\mU-Insurance\\Policy.pdf", isFile=True)
    register_response = register(hash)
    return jsonify(register_response)

@app.route('/hashFile', methods=["GET", "POST"])
def hashFile():
    if request.method == 'GET':
        file_path = "C:\\Development\\Personal\\mU-Insurance\\Policy.pdf"
        hash = getHash(file_path, isFile=True)
        register_response = register(hash)
        return jsonify(register_response)

    # uploaded file
    elif request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return jsonify({
                'status': 'error',
                'message': 'No file present'
            })
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return jsonify({
                'status': 'error',
                'message': 'No filename present'
            })
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            hash = getHash(file_path, isFile=True)
            register_response = register(hash)
            return jsonify(register_response)

@app.route('/verify')
def verifyDocumeny():
    if request.method == 'GET':
        content = request.json
        return jsonify(verify(content))
                   
if __name__ == '__main__':
    app.run(debug=True)