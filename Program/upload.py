from flask import Flask, Blueprint, jsonify, request
from uploadQuery import uploadFiles, getFiles, getFileData, getPublicUrlsOfPlotImages, getPlotImages, GetPublicUrlsOfImages, deleteFile, deleteImage
from Image import FITStoImages
'''
FileName: upload.py

Developer: Kylee B

Description: routes to handle uploads to any specific user using userId as the unique identifier

Routes:
    * /upload/files/<userId>: POST
        request: 
        -JSON:
            file (File Object)
        -params:
            userId
        send:
        -JSON:
            message (String)
    * /files/<userId>: GET
        -params:
            userId
        send:
        -JSON:
            message (String)
            response (Array)
    * /upload/images/<userId>: POST
        request:
            fileName (JSON)
        -params:
            userId
        send:
        -JSON:
            message (String)
            paths (Array)
    * /images/<userId>: GET
        -params:
            userId 
        send:
            -JSON:
                message (String)
                paths (Array)
                filderNames (Array)
                imageNames (Array)
    * /delete/<fileName>/<userId>: DELETE
        -params:
            fileName
            userId
        send:
            -JSON
                message (String)
                response (Array)
    */delete/image: POST
        request:
            imagePath
        send:
            message(String)
            response(Array)

'''


# INIT /upload route
upload_bp = Blueprint('upload', __name__)

 # -- UPLOAD LOGIC --

# UPLOAD the FITS file
@upload_bp.route("/upload/files/<userId>", methods=["POST"])
def upload_files(userId):
    file = request.files['file']
    fileName = file.filename

    response = uploadFiles(userId, file, fileName)
    
    if response:
        return jsonify({"message":"File Upload Successful"}), 200
    else:
        return jsonify({"message": "Error uploading File"}), 401

# For GETTING user files
@upload_bp.route("/files/<userId>", methods=["GET"])
def get_files(userId):

    response = getFiles(userId)

    if response:

        return jsonify({"message":"File retrieval Successful",
                        "response": response,}), 200
    else:
        return jsonify({"message": "Error retrieving Files"}), 401

# For uploading images corresponding to the file
@upload_bp.route("/upload/images/<userId>", methods=["POST"])
def upload_images(userId):
    try:
        data = request.get_json()
        fileName = data.get("name")
        file = getFileData(fileName, userId)
        #print(file)
        response = FITStoImages(file, userId, fileName)
        paths = getPublicUrlsOfPlotImages(response)
        #print(paths)
        if response:
            return jsonify({"message":"Image Generation successful", "paths":paths}), 200       
        else:
            return jsonify({"message": "Error generating images"}), 404   
    except Exception as e:
        return jsonify({"message":f"There are No Images in {fileName}"}), 409
    
# GET ALL user images
@upload_bp.route("/images/<userId>", methods=["GET"])
def get_images(userId):
    try:
        paths, folderNames, imageNames = getPlotImages(userId)
        #print(paths)
        publicUrls =  GetPublicUrlsOfImages(paths)

        if publicUrls:
            return jsonify({"message":"Image retrieval successful", "paths":publicUrls, "folderNames":folderNames, "imageNames": imageNames}), 200       
        else:
            return jsonify({"message": "Error generating public URLs"}), 404
    except Exception as e:
        return jsonify({"message":f"error retrieving images"}), 409
    
# -- DELETE LOGIC --
    
# delete a file from users "files" folder
@upload_bp.route("/delete/<fileName>/<userId>", methods=["DELETE"])
def delete_file(fileName, userId):
    response = deleteFile(fileName, userId)

    if response:
        return jsonify({"message":"File removal Successful",
                        "response": response}), 200
    else:
        return jsonify({"message": "Error removing File"}), 401

# delete a image from users "images" folder
@upload_bp.route("/delete/image", methods=["DELETE", "POST"])
def delete_image():
    data = request.get_json()
    imagePath = data.get("imagePath")
    response = deleteImage(imagePath)
    
    if response:
        return jsonify({"message":"File removal Successful",
                        "response": response}), 200
    else:
        return jsonify({"message": "Error removing File"}), 401