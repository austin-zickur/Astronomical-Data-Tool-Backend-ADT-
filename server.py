
from flask import Flask
from flask_cors import CORS
# Routes: Queries/Users/signup.py
import sys
import os
# Add the directory to the system path
sys.path.append(os.path.abspath("./Queries/Users"))
sys.path.append(os.path.abspath("./Program"))

from user import user_bp
from upload import upload_bp
import os


# Initialize Flask app
app = Flask(__name__)
# CORS(app)
CORS(app, supports_credentials=True)


# Register blueprints (Routes)
app.register_blueprint(user_bp)
app.register_blueprint(upload_bp)

heroku_port = os.environ.get('PORT')
test_port = os.getenv("TEST_PORT") # -- test
# Run the app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=heroku_port, debug=True)