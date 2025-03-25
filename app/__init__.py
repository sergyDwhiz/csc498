from flask import Flask

# Explicitly set the template folder relative to this file.
app = Flask(__name__, template_folder="../templates")

# Import routes to register endpoints
from app import routes
