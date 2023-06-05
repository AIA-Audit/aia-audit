from aia_audit.website.engine import app
from flask import render_template, request
from aia_audit.website.backend.controllers import scancontroller
from aia_audit.website.backend.controllers import settingcontroller
from aia_audit.lib.modules import *
import aia_audit.__main__ as main
import json



#User Routes
@app.route('/')
@app.route('/new/scan')
@app.route('/about')
@app.route('/settings')
@app.route('/scans')
@app.route('/modules')
@app.route('/help')
def show_frontend():
    return render_template('index.html')

@app.route('/scan/<scan_id>')
def show_scan(scan_id):
    return render_template('index.html')

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

@app.route('/api/data/config-status')
def config_status():
    data = {
        "config_status": settingcontroller.config_status()
    }
    return data

@app.route('/api/data/config', methods=['GET'])
def get_config():
    data = settingcontroller.get_config()
    return data

@app.route('/api/data/config', methods=['POST'])
def update_config():
    data = json.loads(request.data)
    settingcontroller.update_config(data)
    return {"status": "success"}

@app.route('/api/data/statistics/total-scans')
def total_scans():
    data = {
        "total_scans": scancontroller.count_all_scans()
    }
    if(data["total_scans"] == None):
        data["total_scans"] = "0"
    return data

@app.route('/api/data/statistics/total-devices')
def total_devices():
    data = {
        "total_devices": scancontroller.count_all_scans_devices()
    }
    if(data["total_devices"] == None):
        data["total_devices"] = "0"
    return data

@app.route('/api/data/statistics/total-vulnerabilities')
def total_vulnerabilities():
    data = {
        "total_vulnerabilities": scancontroller.count_all_scans_vulnerabilities()
    }
    if(data["total_vulnerabilities"] == None):
        data["total_vulnerabilities"] = "0"
    return data

@app.route('/api/data/statistics/last-scan-date')
def last_scan():
    unixtime = scancontroller.get_last_scan_date()
    if unixtime == None:
        data = {
            "last_scan_date": "None"
        }
    else: 
        data = {
            "last_scan_date": scancontroller.get_last_scan_date()
        }
    return data

@app.route('/api/data/scan/<scan_id>', methods=['GET'])
def get_scan(scan_id):
    data = scancontroller.get_scan(scan_id)
    json_data = []
    for scan in data:
        json_data.append({
            "id": scan[0],
            "name": scan[1],
            "target": scan[2],
            "start_time": scan[3],
            "end_time": scan[4],
            "results": scan[5]
        })
    return json_data

@app.route('/api/data/scans', methods=['GET'])
def get_scans():
    data = scancontroller.get_scans()
    json_data = []
    for scan in data:
        json_data.append({
            "id": scan[0],
            "name": scan[1],
            "target": scan[2],
            "start_time": scan[3],
            "end_time": scan[4],
            "results": scan[5]
        })
    return json_data

@app.route('/api/data/scans/last/5', methods=['GET'])
def get_last_scans():
    data = scancontroller.get_last_scans()
    json_data = []
    for scan in data:
        json_data.append({
            "id": scan[0],
            "name": scan[1],
            "target": scan[2],
            "start_time": scan[3],
            "end_time": scan[4],
            "results": scan[5]
        })
    return json_data

@app.route('/api/data/modules', methods=['GET'])
def get_modules():
    data = get_modules_from_folder()
    return data

@app.route('/api/data/active-modules', methods=['GET'])
def get_active_modules():
    data = get_modules_from_database()
    return data

@app.route('/api/install-module', methods=['POST'])
def install_module():
    data = json.loads(request.data)
    install_module_from_folder(data["module"])
    return {"status": "success"}

@app.route('/api/uninstall-module', methods=['POST'])
def uninstall_module():
    data = json.loads(request.data)
    uninstall_module_from_database(data["module"])
    return {"status": "success"}

@app.route('/api/save-module-settings', methods=['POST'])
def save_module_settings():
    print("save_module_settings")
    data = json.loads(request.data)
    database = Database()
    database.query("UPDATE modules SET settings = '" + json.dumps(data["settings"]) + "' WHERE name = '" + data["module"] + "'")
    return {"status": "success"}

@app.route('/api/scan/start', methods=['POST'])
def start_scan():
    if(main.status == main.TOOL_STATUS_SCANNING):
        return {"status": "error", "message": "There is already a scan running"}
    data = json.loads(request.data)
    scancontroller.start_scan(data)
    return {"status": "success"}

@app.route('/api/telegram/handler', methods=['POST'])
def telegram_handler():
    data = request.get_json()
    chat_id = data['message']['chat']['id']
    message_text = data['message']['text']
    print("[*] Telegram message received from chat ID " + str(chat_id) + ": " + message_text)
    main.telegram.process_message(chat_id, message_text)
    return 'OK'