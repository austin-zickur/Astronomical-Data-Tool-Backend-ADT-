from flask import Flask
# Routes: Queries/Users/signup.py
import sys
print("Python search paths:")
for path in sys.path:
    print(path)
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