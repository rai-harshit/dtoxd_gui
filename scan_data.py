from datetime import datetime
import platform
from psutil import virtual_memory
import requests

def send_scan_results(scan_datetime,scan_duration,files_scanned_count,files_explicit_count,scan_type):
    # Collect all the details to send.
    specs = platform.uname()
    memory = virtual_memory().total/1024**3
    scan_datetime = ""
    scan_duration = ""
    files_scanned_count = ""
    files_explicit_count = ""
    scan_type = ""
    data = {
    'specs':str(specs),
    'memory':str(memory),
    'scan_datetime':scan_datetime,
    'scan_duration':scan_duration,
    'files_scanned_count':files_scanned_count,
    'files_explicit_count':files_explicit_count,
    'scan_type':scan_type
}
    data=json.dumps(data, indent=2)
#     data=json.loads(data)
    response=requests.post('https://dtoxd-data.appspot.com/api',json=data)
    if(response.status_code==200):
        print("successfull")
        


