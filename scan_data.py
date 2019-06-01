import platform
from psutil import virtual_memory
import requests
import json

def send_scan_results(scan_details):
    # Collect all the details to send.
    print(scan_details)

    specs = platform.uname()
    memory = virtual_memory().total/1024**3
    scan_start_datetime = scan_details['scan_start_datetime']
    scan_end_datetime = scan_details['scan_end_datetime']
    files_scanned_count = scan_details['total_images_scanned']
    files_explicit_count = scan_details['total_explicit_images']
    scan_type = scan_details['scan_type']
    scan_status = scan_details['scan_status']
    data = {
    'machine_specs':str(specs),
    'ram_memory':str(memory),
    'scan_start_datetime':str(scan_start_datetime),
    'scan_end_datetime':str(scan_end_datetime),
    'scanned_images_count':str(files_scanned_count),
    'explicit_images_count':str(files_explicit_count),
    'scanned_videos_count':str(""),
    'explicit_videos_count':str(""),
    'scan_type':scan_type,
    'scan_status':scan_status
}
    data=json.dumps(data, indent=2)
#     data=json.loads(data)
    response=requests.post('https://dtoxd-data-242316.appspot.com/api',json=data)
    print(response.status_code)
    if(response.status_code==200):
        print("successfull")
        


