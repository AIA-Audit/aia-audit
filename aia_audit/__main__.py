#!/usr/bin/env python3
import sys, threading
from aia_audit.lib import gui
from aia_audit.lib.config import Config
from aia_audit.constants import *
from aia_audit.lib.database import Database
from aia_audit.website.engine import Website
from flask import Flask
from time import sleep


version = "0.0.1"
status = TOOL_STATUS_WAITING

def main():
    try:
        #Start the GUI
        gui.show_loading()
        sleep(5)
        gui.clear()
        print("[*] Starting the AIA Audit framework ... Done!")
        #Start the config
        config = Config()
        config.config_start()
        #Start the database
        database = Database("aia_audit/data/database.db")
        #Start the website
        website = Website(config, database)
        website.website_start()
        gui.show_running(config.website_address, config.website_port)
        #Prevent the main thread from exiting
        while not status == TOOL_STATUS_SHUTDOWN:
            sleep(1)

    except KeyboardInterrupt:
        gui.clear()
        print("[*] Exiting the AIA Audit framework ... Done!")
        sys.exit(0)