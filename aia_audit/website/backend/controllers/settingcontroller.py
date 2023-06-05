from aia_audit.lib.database import Database

def config_status():
    database = Database()
    result = database.query_select("SELECT value FROM settings WHERE name = 'config_status'")[0][0]
    if result == "1":
        return True
    else:
        database.query("UPDATE settings SET value = '1' WHERE name = 'config_status'")
        return False
    
def get_config():
    database = Database()
    config = {}
    config["website_address"] = database.query_select("SELECT value FROM settings WHERE name = 'website_address'")[0][0]
    config["website_port"] = database.query_select("SELECT value FROM settings WHERE name = 'website_port'")[0][0]
    config["telegram_notify"] = database.query_select("SELECT value FROM settings WHERE name = 'telegram_notify'")[0][0]
    config["telegram_token"] = database.query_select("SELECT value FROM settings WHERE name = 'telegram_token'")[0][0]
    return config

def update_config(config):
    database = Database()
    database.query("UPDATE settings SET value = '{}' WHERE name = 'website_address'".format(config["website_address"]))
    database.query("UPDATE settings SET value = '{}' WHERE name = 'website_port'".format(config["website_port"]))
    database.query("UPDATE settings SET value = '{}' WHERE name = 'telegram_notify'".format(config["telegram_notify"]))
    database.query("UPDATE settings SET value = '{}' WHERE name = 'telegram_token'".format(config["telegram_token"]))
