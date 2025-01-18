from flask import Flask
from signup import user_bp


# Initialize Flask app
app = Flask(__name__)


# Register blueprints
#app.register_blueprint(user_bp, url_prefix='/adt-api')
app.register_blueprint(user_bp)
#app.register_blueprint(post_bp, url_prefix='/api')

# Run the app
if __name__ == '__main__':
    app.run(port=8000, debug=True)