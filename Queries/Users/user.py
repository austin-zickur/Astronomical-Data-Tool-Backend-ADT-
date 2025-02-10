from flask import Flask, Blueprint, jsonify, request

# import signup() from Queries/Users/signup.py
from userQueries import signUp, getEmails

# INIT /user route
user_bp = Blueprint('user', __name__)


'''
FileName: SignUp !!

Developer: Kylee B

Description: routes to handle user Authentification including
             signUp, signIn, SignOut, Delete User

Routes:
    * /user/signUp: POST
        request: 
        -JSON:
            email (String)
            password (String)
        send:
        -JSON:
            message (String)

    * /user/check-if-user-exists/<email>: GET
        request:
        -Params: 
            email
        send:
        -JSON:
            Message (String)
'''

# SIGN UP user to Astronomival Data Plotter
@user_bp.route("/user/sign-up", methods=["POST"])
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
    
# Check if user already exists 
@user_bp.route("/user/check-if-user-exists/<email>", methods=["GET"])
def check_user(email):
    userEmails = getEmails()
    if userEmails:
        if email in userEmails:
            return jsonify({"message":"user already exists"}), 401
        else:
            return jsonify({"message":"user not in system, sign up successful"}), 200
    else:
        return jsonify({"message":"Error fetching emails"}), 401
    

'''
-- UNUSED --  -- UNUSED --  -- UNUSED --  -- UNUSED -- 
@user_bp.route("/user/sign-in", methods=["POST"])
def sign_in():
    try:
        data = request.get_json()

        if data:
            email = data.get("email")
            password = data.get("password")

            access_token = signIn(email, password)
            
            if access_token:
                return jsonify({
                    "message":"User SignIn Successful",
                    "token":access_token
                }), 200

        else:
            return jsonify({"message":"Invalid Credentials"}), 401
    except Exception as e:
        return jsonify({"message": "Error signing in", "error": str(e)}), 500
'''

#DEBUG BELOW:
'''
TEST ROUTE
@user_bp.route("/user/test/", methods=["GET"])
def test():
    return jsonify({"message":"this is a test"}), 200
'''

