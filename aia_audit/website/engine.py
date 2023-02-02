from flask import Flask, render_template, cli
import logging, threading, os

app = Flask(__name__, static_url_path='', static_folder='./frontend/dist', template_folder="./frontend/dist")

#Import flask routes file to handle all the requests
from aia_audit.website.routes import *

class Website:

    thread = None

    def _disabled_server_banner(*args, **kwargs):
        pass

    def website_start(self, config):
        logging.getLogger("werkzeug").disabled = True
        cli.show_server_banner = self._disabled_server_banner
        thread = threading.Thread(target=lambda: app.run(host=config.website_address, port=config.website_port, debug=False, use_reloader=False))
        thread.setDaemon(True)
        thread.start()
        self.thread = thread
