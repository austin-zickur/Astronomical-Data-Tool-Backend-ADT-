
from flask import Flask
# Routes: Queries/Users/signup.py
import sys
import os
# Add the directory to the system path
sys.path.append(os.path.abspath("./Queries/Users"))
sys.path.append(os.path.abspath("./Program"))

from signup import user_bp
from upload import upload_bp


# Initialize Flask app
app = Flask(__name__)


# Register blueprints (Routes)
app.register_blueprint(user_bp)
app.register_blueprint(upload_bp)


# Run the app
if __name__ == '__main__':
    app.run(port=8000, debug=True)