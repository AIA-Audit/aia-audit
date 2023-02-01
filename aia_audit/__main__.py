#!/usr/bin/env python3
import sys, threading
from aia_audit.lib import gui
from aia_audit.lib.config import Config
from aia_audit.website.engine import Website
from flask import Flask
from time import sleep

version = "0.0.1"

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
        #Start the website
        website = Website()
        website.website_start(config)
        #Prevent the main thread from exiting
        while True:
            sleep(1)

    except KeyboardInterrupt:
        gui.clear()
        print("[*] Exiting the AIA Audit framework ... Done!")
        sys.exit(0)