from aia_audit.website.engine import app
from flask import render_template
import aia_audit.__main__ as main
import json



#User Routes
@app.route('/')
@app.route('/about')
def show_frontend():
    return render_template('index.html')

#API routes
@app.route('/api/data/tool-info')
def tool_info():
    data = {
        "status": main.status,
        "version": main.version
    }
    return data

@app.route('/api/data/statistics/total-scans')
def total_scans():
    data = {
    }
    return data