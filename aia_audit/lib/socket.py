import logging, threading, os
from time import sleep
from flask import Flask, cli
from flask_socketio import SocketIO, emit
import aia_audit.__main__ as main

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

class Socket:

    #Send message to the client
    def send_message(self, message, type='info'):
        socketio.emit('message', {'content': message, 'type': type})

    def __init__(self):
        print ("[*] Loading the socket ...")
        thread = threading.Thread(target=lambda: socketio.run(app, host='localhost', port=8989))
        thread.setDaemon(True)
        thread.start()

socket = Socket()

@socketio.on('connect') 
def handle_connect(self):
    socket.send_message('Connected to the server', 'success')
    if(main.status == main.TOOL_STATUS_WAITING):
        socket.send_message('Waiting for the user to start the scan ...', 'info')
    elif(main.status == main.TOOL_STATUS_SCANNING):
        socket.send_message('There is already a scan running, please wait ...', 'info')
    
@socketio.on('disconnect')
def handle_disconnect():
    socket.send_message('Disconnected from the server', 'status')