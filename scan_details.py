from datetime import datetime
import platform
from psutil import virtual_memory

def send_scan_results(scan_datetime,scan_duration,files_scanned_count,files_explicit_count,scan_type):
	# Collect all the details to send.
	specs = platform.uname()
	memory = virtual_memory().total/1024**3
	scan_datetime = ""
	scan_duration = ""
	files_scanned_count = ""
	files_explicit_count = ""
	scan_type = ""

	# Convert the data in the appropriate format.

	# Create connection with the server and send the scan results to the server.

