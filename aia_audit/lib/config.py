from aia_audit.lib.database import Database

class Config:

    website_address = "0.0.0.0"
    website_port = "5000"
    configured = "no"

    def __init__(self):
        self.config_start()

    def config_start(self):
        print ("[*] Loading the configuration ...")
        database = Database()
        self.website_address = database.query_select("SELECT value FROM settings WHERE name = 'website_address'")[0][0]
        self.website_port = database.query_select("SELECT value FROM settings WHERE name = 'website_port'")[0][0]
        self.configured = database.query_select("SELECT value FROM settings WHERE name = 'config_status'")[0][0]
        
        