# i = 0
# j = 0
# count = 0
# for i in range(1000):
# 	if count>=10000:
# 		break
# 	for j in range(1000):
# 		count+=1
# 		print("count : {}".format(count))
# 	print("i : {}".format(i))
import scan_data
test={}
test['scan_start_datetime']="1822312"
test['scan_end_datetime']="1822312"
test['total_images_scanned']="15"
test['total_explicit_images']="10"
test['scan_type']="Quick"
scan_data.send_scan_results(test)
