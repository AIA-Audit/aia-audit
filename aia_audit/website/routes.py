from aia_audit.website.engine import app
from flask import render_template
from aia_audit.website.backend.controllers import scancontroller
import aia_audit.__main__ as main
import json



#User Routes
@app.route('/')
@app.route('/about')
def show_frontend():
    return render_template('index.html')

#API routes
@app.route('/api/stop-tool')
def stop_tool():
    main.status = main.TOOL_STATUS_SHUTDOWN
    return "success"

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
        "total_scans": scancontroller.count_all_scans()
    }
    return data

@app.route('/api/data/statistics/total-devices')
def total_devices():
    data = {
        "total_devices": scancontroller.count_all_scans()
    }
    return data

@app.route('/api/data/statistics/total-vulnerabilities')
def total_vulnerabilities():
    data = {
        "total_vulnerabilities": scancontroller.count_all_scans()
    }
    return data

@app.route('/api/data/statistics/last-scan')
def last_scan():
    data = {
        "last-scan": scancontroller.count_all_scans()
    }
    return data