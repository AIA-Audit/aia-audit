import requests

def get_data(cve):
    data = requests.get('https://cve.circl.lu/api/cve/' + cve)
    if data.status_code == 200:
        return data.json()
    else :
        return None
