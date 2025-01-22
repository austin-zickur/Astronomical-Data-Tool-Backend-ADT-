from flask import Flask, Blueprint, jsonify, request
from uploadQuery import uploadFiles, getFiles, uploadImages
from Image import FITStoImages
'''
FileName: SignUp

Developer: Kylee B

Description: routes to handle user Authentification including
             signUp, signIn, SignOut, Delete User

Routes:
    * /upload/files/: POST
        request: 
            file (File Object)
            user (String)
        send:
            message (String)

'''


# INIT /upload route
upload_bp = Blueprint('upload', __name__)

@upload_bp.route("/upload/files/<userId>", methods=["POST"])
def upload_files(userId):
    file = request.files['file']
    fileName = file.filename

    response = uploadFiles(userId, file, fileName)
    
    if response:
        return jsonify({"message":"File Upload Successful"}), 200
    else:
        return jsonify({"message": "Error uploading File"}), 401

# For GETTING files

@upload_bp.route("/files/<userId>", methods=["GET"])
def get_files(userId):

    response = getFiles(userId)
    
    if response:
        return jsonify({"message":"File retrieval Successful",
                        "response": response}), 200
    else:
        return jsonify({"message": "Error retrieving Files"}), 401

#
@upload_bp.route("/upload/images/<userId>", methods=["POST"])
def upload_images(userId):
    file = request.files['file']
    fileName = file.filename

    dataList = FITStoImages(file)
    response = uploadImages(dataList, userId, fileName)
    #response = getFiles(userId)
    
    if response:
        return jsonify({"message":"File retrieval Successful"}), 200
    else:
        return jsonify({"message": "Error retrieving Files"}), 401
