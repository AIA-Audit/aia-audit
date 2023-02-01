# Get the app object from the __init__.py file
from aia_audit.website.engine import app
from flask import render_template

@app.route('/')
def hello_world():
    return render_template('index.html')