#!/usr/bin/env python3
import sys, threading
from aia_audit.lib import gui
from flask import Flask
from aia_audit.website.engine import Website
from time import sleep


def main():
    try:
        #Start the GUI
        gui.show_loading()
        sleep(5)
        gui.clear()
        print("[*] Starting the AIA Audit framework ... Done!")
        #TODO: DATABASE LOAD / CREATE (SQLITE)
        #Start the website
        website = Website()
        website.website_start()
        #Prevent the main thread from exiting
        while True:
            sleep(1)

    except KeyboardInterrupt:
        gui.clear()
        print("[*] Exiting the AIA Audit framework ... Done!")
        sys.exit(0)