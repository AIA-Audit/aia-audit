import os
import time
import aia_audit.__main__ as main

from aia_audit.lib.database import Database

class Scan:
    type = None
    start_time = int(time.time())
    end_time = None
    target = None
    targetType = None
    modules = None
    results = None
    total_devices = 0
    total_devices_array = None
    total_vulnerabilities = 0

    def __init__(self, target, targetType, modules, type):
        self.results = []
        self.total_devices_array = []
        self.target = target
        self.targetType = targetType
        self.modules = modules
        self.type = type

    def start(self):
        main.status = main.TOOL_STATUS_SCANNING
        main.socket.send_message('Starting scan, please wait ...', 'info')
        time.sleep(4)
        main.socket.send_message('Scan started at ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.start_time)), 'status')
        time.sleep(1)
        main.socket.send_message('Scan Target: ' + self.target, 'info')
        time.sleep(1)
        if(self.type == 1):
            main.socket.send_message('Scan Type: Reconnaissance', 'info')
            if(self.targetType == 1):
                response = os.system("ping -c 1 " + self.target)
                if response == 0:
                    ttl = os.popen("ping -c 1 " + self.target + " | grep ttl").read()
                    main.socket.send_message('Target ' + self.target + ' is up!', 'success')
                    self.add_scan_module({"name": "Ping", "devices": []})
                    self.add_scan_device_to_module({"ip": self.target, "vulnerabilities": []})
                    self.add_scan_device_vulnerability({"name": "Device status", "description": "Ping the target to check if it is up", "severity": "info", "type": "ping", "output": "Target is up!\n\n" + ttl})
                else:
                    main.socket.send_message('Target ' + self.target + ' is down!', 'error')
                    self.add_scan_module({"name": "Ping", "devices": []})
                    self.add_scan_device_to_module({"ip": self.target, "vulnerabilities": []})
                    self.add_scan_device_vulnerability({"name": "Device status", "description": "Ping the target to check if it is up", "severity": "info", "type": "ping", "output": "Target is down"})
                self.store_scan()
            if(self.targetType == "2"):
                _target = self.target.split(".")
                ip = _target[0] + "." + _target[1] + "." + _target[2]
                self.add_scan_module({"name": "Ping", "devices": []})
                for i in range(1, 255):
                    response = os.system("ping -c 1 " + ip + "." + str(i))
                    if response == 0:
                        ttl = os.popen("ping -c 1 " + ip + "." + str(i) + " | grep ttl").read()
                        main.socket.send_message('Target ' + ip + "." + str(i) + ' is up!', 'success')
                        self.add_scan_device_to_module({"ip": ip + "." + str(i), "vulnerabilities": []})
                        self.add_scan_device_vulnerability({"name": "Device status", "description": "Ping the target to check if it is up", "severity": "info", "type": "ping", "output": "Target is up! \n\n" + ttl})
                    else: 
                        main.socket.send_message('Target ' + ip + "." + str(i) + ' is down!', 'error')
                self.store_scan()
        elif(self.type == 2):
            main.socket.send_message('Scan Type: Modular', 'info')
            modules_string = ''
            for module in self.modules:
                modules_string += module["name"]
                if module != self.modules[-1]:
                    modules_string += ', '
            main.socket.send_message('Modules: ' + modules_string, 'info')
            self.run_next_module()
        
    def run_next_module(self):
        module = self.modules[0]
        self.modules.pop(0)
        mod_file =  __import__(module["import"] + '.main', fromlist=[''])
        mod_file.main(self.target)
        if len(self.modules) > 0:
            self.run_next_module()
        else:
            self.store_scan()

    def add_scan_module(self, module):
        self.results.append(module)
    
    def add_scan_device_to_module(self, device):
        self.results[-1]["devices"].append(device)
        if device["ip"] not in self.total_devices_array:
            self.total_devices_array.append(device["ip"])
        self.total_devices = len(self.total_devices_array)

    def add_scan_device_vulnerability(self, vulnerability):
        self.results[-1]["devices"][-1]["vulnerabilities"].append(vulnerability)
        self.total_vulnerabilities += 1

    def store_scan(self):
        print("Called")
        main.status = main.TOOL_STATUS_WAITING
        self.end_time = int(time.time())
        main.socket.send_message('Scan completed at ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.end_time)), 'success')
        # Search output key in the results 
        for item in self.results:
            for device in item["devices"]:
                for vulnerability in device["vulnerabilities"]:
                    if "output" in vulnerability:
                        # Replace the output key, value with parsed output
                        vulnerability["output"] = vulnerability["output"].replace("'", "`")
        self.results = str(self.results).replace("'", "\"")
        if(self.type == 1):
            name = "Reconnaissance Scan"
        elif(self.type == 2):
            name = "Modular Scan"
        database = Database()
        database.insert("scans", "name, target, start_time, end_time, results, devices, vulnerabilities", "'" + name + "','" + str(self.target) + "', '" + str(self.start_time) + "', '" + str(self.end_time) + "', '"+ self.results +"', '" + str(self.total_devices) + "', '" + str(self.total_vulnerabilities) + "'")
        main.socket.send_message('Scan stored in the database', 'success')
        if(main.telegram.enabled == "True"):
            main.telegram.notify_scan_finished(self.total_devices, self.total_vulnerabilities)