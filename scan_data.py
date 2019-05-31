import platform
from psutil import virtual_memory
import requests
import json

def send_scan_results(scan_details):
    # Collect all the details to send.
    print(scan_details)

    specs = platform.uname()
    memory = virtual_memory().total/1024**3
    scan_datetime = scan_details['scan_start_datetime']
    scan_end_datetime = scan_details['scan_end_datetime']
    files_scanned_count = scan_details['total_images_scanned']
    files_explicit_count = scan_details['total_explicit_images']
    scan_type = scan_details['scan_type']
    complete = "NA"
    data = {
    'specs':str(specs),
    'memory':str(memory),
    'scan_datetime':str(scan_datetime),
    'scan_end_datetime':str(scan_end_datetime),
    'files_scanned_count':files_scanned_count,
    'files_explicit_count':files_explicit_count,
    'scan_type':scan_type,
    'complete':complete
}
    data=json.dumps(data, indent=2)
#     data=json.loads(data)
    response=requests.post('https://dtoxd-data.appspot.com/api',json=data)
    print(response.status_code)
    if(response.status_code==200):
        print("successfull")
        


