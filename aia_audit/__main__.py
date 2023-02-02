#!/usr/bin/env python3
import sys
from aia_audit.lib import gui
from aia_audit.lib.config import Config
from aia_audit.constants import *
from aia_audit.lib.database import Database
from aia_audit.website.engine import Website
from flask import Flask
from time import sleep

config = None
status = TOOL_STATUS_WAITING
version = "0.1"

def main():
    try:
        #Show loading screen
        gui.show_loading()
        sleep(5)
        gui.clear()
        #Load the tool configuration and start the website engine
        global config, database_path, status
        config = Config()
        database = Database()
        database.check_database()
        Website(config, database)
        gui.show_running(config.website_address, config.website_port)
        #Prevent the main thread from exiting
        while not status == TOOL_STATUS_SHUTDOWN:
            sleep(1)

    except KeyboardInterrupt:
        gui.clear()
        print("[*] Exiting the AIA Audit framework ... Done!")
        sys.exit(0)