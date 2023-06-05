import nmap
import aia_audit.__main__ as _main

def main(target, settings = None):
    _main.socket.send_message('Starting NMAP scanner ...', 'module')
    _main.scan.add_scan_module({"name": "NMAP", "devices": []})
    nmapScanner = nmap.PortScanner()
    nmapScanner.scan(target, arguments='-sV -A')
    nmap_xml_output = nmapScanner.get_nmap_last_output()
    scan_result = nmapScanner.analyse_nmap_xml_scan(nmap_xml_output)
    scan_result = str.replace(str(scan_result), '"', "'")
    _main.scan.add_scan_device_to_module({"ip": target, "vulnerabilities": []})
    _main.scan.add_scan_device_vulnerability({"name": "Scan console output", "description": "Parsed console output from NMAP", "severity": "info", "type": "output", "output": str(scan_result)})
    return {"status": "success", "result": {}}
