import requests
import aia_audit.__main__ as _main
import shodan

def main(target):
    _main.socket.send_message('Starting Shodan scanner ...', 'module')
    _main.scan.add_scan_module({"name": "Shodan", "devices": []})
    api_key = 'ttIwkVmHcyFprQy6F5WntZSWLVzUkswn'
    url = 'https://api.shodan.io/shodan/host/' + target + '?key=' + api_key
    data = requests.get(url)
    if data.status_code == 200:
        print(data.json())
        _main.scan.add_scan_device_to_module({"ip": target, "vulnerabilities": []})
        _main.scan.add_scan_device_vulnerability({"name": "Shodan scan", "description": "Shodan scan", "severity": "info", "type": "output", "output": str(data.json())})
    else:
        _main.socket.send_message('Shodan scan failed', 'error')
        print(data.status_code)
        print(data.text)
    return {"status": "success", "result": {}}