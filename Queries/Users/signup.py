from flask import Flask, Blueprint, jsonify, request

# import signup() from Queries/Users/signup.py
from userQueries import signUp, signIn

# INIT /user route
user_bp = Blueprint('user', __name__)


'''
FileName: SignUp !!

Developer: Kylee B

Description: routes to handle user Authentification including
             signUp, signIn, SignOut, Delete User

Routes:
    * /user/signUp/: POST
        request: 
            JSON
                email (String)
                password (String)
        send:
            message (String)

'''

@user_bp.route("/user/sign-up/", methods=["POST"])
def sign_up():
    # request JSON data from user
    data = request.get_json()

    if data:

        fullName = data.get("fullName")
        email = data.get("email")
        password = data.get("password")
        # use signUp to return success
        response = signUp(fullName, email, password)

        #print("user signed up successfully")
        return jsonify({
            "message":"User SignUp Successful"
        }), 200
    else:
        return jsonify({"message":"Invalid Credentials"}), 401

@user_bp.route("/user/signIn/", methods=["POST"])
def sign_in():

    data = request.get_json()

    if data:
        email = data.get("email")
        password = data.get("password")

        response = signIn(email, password)

        return jsonify({
            "message":"User SignIn Successful"
        }), 200
    else:
        return jsonify({"message":"Invalid Credentials"}), 401



'''
TEST ROUTE
@user_bp.route("/user/test/", methods=["GET"])
def test():
    return jsonify({"message":"this is a test"}), 200
'''

