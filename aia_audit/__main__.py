#!/usr/bin/env python3
import sys
from aia_audit.lib import gui
from aia_audit.lib.config import Config
from aia_audit.constants import *
from aia_audit.lib.database import Database
from aia_audit.lib.socket import socket as _socket
from aia_audit.lib.telegram import Telegram
from aia_audit.website.engine import Website
from flask import Flask
from time import sleep

config = None
database = None
scan = None
socket = _socket
telegram = None
status = TOOL_STATUS_WAITING
version = "0.1"

def main():
    try:
        gui.show_loading()
        gui.clear()
        database = Database()
        database.check_database()
        global config, telegram
        config = Config()
        telegram = Telegram()
        if telegram.check_enabled() == "True":
            print("[*] Telegram notifications are enabled")
            telegram.open()
        Website(config, database)
        gui.show_running(config.website_address, config.website_port)
        #Prevent the main thread from exiting
        while not status == TOOL_STATUS_SHUTDOWN:
            sleep(1)
        print("[*] Shutting down the AIA Audit framework ... Done!")

    except KeyboardInterrupt:
        gui.clear()
        print("[*] Exiting the AIA Audit framework ... Done!")
        if telegram.check_enabled() == "True":
            telegram.stop()
        sys.exit(0)