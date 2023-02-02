from aia_audit.lib.database import Database

def count_all_scans():
    database = Database()
    return database.query_select("SELECT COUNT(*) FROM scans")[0][0]
