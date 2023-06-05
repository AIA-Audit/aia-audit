import json
import re
import nmap
import aia_audit.__main__ as _main
import aia_audit.lib.cve_search as cve_search

def main(target, settings = None):
    _main.socket.send_message('Starting NMAP scanner ...', 'module')
    _main.scan.add_scan_module({"name": "NMAP", "devices": []})
    nmapScanner = nmap.PortScanner()
    nmapScanner.scan(target, arguments='-sV -A --script vulners')
    nmap_xml_output = nmapScanner.get_nmap_last_output()
    scan_result = nmapScanner.analyse_nmap_xml_scan(nmap_xml_output)
    _main.scan.add_scan_device_to_module({"ip": target, "vulnerabilities": []})
    extract_scan_info(scan_result)
    return {"status": "success", "result": {}}

def extract_scan_info(json_data):
    data = json_data
    for host_data in data["scan"].values():
        tcp_data = host_data["tcp"]
        for port, port_info in tcp_data.items():
            tmp_port_info = port_info
            #if "script" in port_info:
             #   tmp_port_info.pop("script")
            _main.scan.add_scan_device_vulnerability({"name": f"Open port {str(port)}", "description": "Open port found during NMAP scan", "severity": "info", "type": "output", "output": format_data_for_display(tmp_port_info)})
            if "script" in port_info:
                for script_name, script_info in port_info["script"].items():
                    if script_name == "vulners":
                        extract_cves(script_info, port)


def format_data_for_display(data):
    formatted_text = "Port information:\n"
    if isinstance(data, dict):
        for key, value in data.items():
            formatted_text += f"    {key}: {value}\n"
    else:
        formatted_text = str(data)
    formatted_text = str.replace(str(formatted_text), '"', "'")
    return formatted_text

def extract_cves(json_string, port):
    cve_pattern = r"CVE-\d{4}-\d{4,7}\s+\d+\.\d+\s+https:\/\/vulners\.com\/cve\/CVE-\d{4}-\d{4,7}"
    cves = re.findall(cve_pattern, json_string)
    for cve in cves:
        cve_data = cve.split("\t")
        cve_name = cve_data[0]
        cve_score = cve_data[1]
        cve_url = cve_data[2]
        cve_severity = get_severity(float(cve_score))
        cve_remote = cve_search.get_data(cve_data[0])
        cve_output = f"Score: {cve_score}\nURL: {cve_url}"
        if(cve_remote != None):
            if(cve_remote["capec"] != None):
                if(cve_remote["capec"] is not None and len(cve_remote["capec"]) > 0):
                    if(cve_remote["capec"][0]["name"] != None):
                        cve_name = cve_remote["capec"][0]["name"]
            if(cve_remote["summary"] != None):
                cve_output += "\n\n" + str.replace(cve_remote["summary"], '"', "'")
        _main.scan.add_scan_device_vulnerability({"name": cve_name, "description": f"Vulnerability found during NMAP scan on port {port}", "severity": cve_severity, "type": "cve", "output": cve_output})
    return cves

def get_severity(cve_score):
    if cve_score >= 9:
        return "critical"
    elif cve_score >= 7:
        return "high"
    elif cve_score >= 4:
        return "medium"
    elif cve_score >= 0:
        return "low"
    else:
        return "info"

