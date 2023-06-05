from aia_audit.lib.database import Database
from aia_audit.lib.scan import Scan
import aia_audit.__main__ as main

def count_all_scans():
    database = Database()
    return database.query_select("SELECT COUNT(*) FROM scans")[0][0]

def count_all_scans_devices():
    database = Database()
    return database.query_select("SELECT SUM(devices) FROM scans")[0][0]

def count_all_scans_vulnerabilities():
    database = Database()
    return database.query_select("SELECT SUM(vulnerabilities) FROM scans")[0][0]

def get_last_scan_date():
    database = Database()
    if database.query_select("SELECT start_time FROM scans ORDER BY id DESC LIMIT 1") == []:
        return None
    else:
        return database.query_select("SELECT start_time FROM scans ORDER BY id DESC LIMIT 1")[0][0]

def get_scan(scan_id):
    database = Database()
    return database.query_select("SELECT * FROM scans WHERE id = " + str(scan_id))

def get_last_scans():
    database = Database()
    return database.query_select("SELECT * FROM scans ORDER BY id DESC LIMIT 5")

def get_scans():
    database = Database()
    return database.query_select("SELECT * FROM scans ORDER BY id DESC")

def start_scan(data):
    main.scan = Scan(data["target"], data["targetType"], data["modules"], data["type"])
    main.scan.start()
