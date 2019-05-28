i = 0
j = 0
count = 0
for i in range(1000):
	if count>=10000:
		break
	for j in range(1000):
		count+=1
		print("count : {}".format(count))
	print("i : {}".format(i))