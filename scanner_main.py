# import os
# from multiprocessing import Queue
# import threading
# import cv2 as cv
# import keras
# from keras.models import load_model
# import numpy as np
# from keras.backend import clear_session
# import logging
# import uuid
# import pickle
# import shutil
# import win32api
import time

class Scanner():

	def __init__(self):
		pass

	# test cases
	# Deep Scan
	def DeepScan(self):
		print("Deep Scan Started -- Jaadiye ka Deep Scan wala code.")
		print("Idhar apne maal ka Deep Scan ho raha hai.")
		time.sleep(15)
		print("Deep Scan Completed")


	def QuickScan(self):
		print("Quick Scan Started -- Jaadiye ka Quick Scan wala code.")
		print("Idhar apne maal ka Quick Scan ho raha hai.")
		time.sleep(7)
		print("Quick Scan Completed")

	def Prediction(self):
		print("Prediction Started -- Jaadiye ka Prediction wala code.")
		print("Idhar apne maal ka prediction hoga.")
		time.sleep(10)
		print("Prediction Completed")

	def Quarantine(self):
		print("Quarantine Started -- Jaadiye ka Quarantine wala code")
		print("Abb idhar apna maal quarantine hoga.")
		time.sleep(16)
		print("Quarantine Completed")



	# def Scan(self):
	# 	drives = win32api.GetLogicalDriveStrings()
	# 	drives = drives.split('\000')[:-1]
	# 	for drive in drives:
	# 		for (root,dirs,files) in os.walk(drive, topdown=True): 
	# 			global thread_stop
	# 			if(thread_stop==True):
	# 				break
	# 		    # print("root",root) 
	# 		    # print("dir",dirs) 
	# 		    # print("files:",files) 
	# 			if(len(files)!=0):
	# 				for i in files:
	# 					if(i.endswith(".jpg") or i.endswith(".png") or i.endswith(".bmp") or i.endswith(".jpeg")):
	# 						data.put(root+"/"+i)
	# 	data.put("XOXO")

	# def QuickScan(self):
	# 	drives = win32api.GetLogicalDriveStrings()
	# 	drives = drives.split('\000')[:-1]
	# 	drives[0]=os.path.expanduser("~")
	# 	for drive in drives:
	# 		for (root,dirs,files) in os.walk(drive, topdown=True): 
	# 			global thread_stop
	# 			if(thread_stop==True):
	# 				break
	# 		    # print("root",root) 
	# 		    # print("dir",dirs) 
	# 		    # print("files:",files) 
	# 			if(len(files)!=0):
	# 				for i in files:
	# 					if(i.endswith(".jpg") or i.endswith(".png") or i.endswith(".bmp") or i.endswith(".jpeg")):
	# 						data.put(root+"/"+i)
	# 	data.put("XOXO")


	# def Predict(self):
	# 	x=""
	# 	model = load_model("model.h5")
	# 	while(x!="XOXO"):
	# 		global thread_stop
	# 		if(thread_stop==True):
	# 			break
	# 		x=data.get()
	# 		if(x!="" or x is not None):
	# 			img=cv.imread(x)
	# 			if(img is not None):
	# 				''' There is no need to check if the size is not 300 x 300 because most of the files wont be of that size and we'll be wasting
	# 				# out time checking conditions everytime'''
	# 				# height, width = img.shape[:2]
	# 				# if(height>300 and width>300) or (height<300 and width<300):
	# 				img=cv.resize(img,(300,300))
	# 				img=np.array(img)
	# 				image = np.reshape(img,(1,300,300,3))
	# 				# clear_session()
	# 				l=model.predict(image)
	# 				if(l[0][0]>l[0][1]):
	# 					explicitfiles.put(x)
	# 	explicitfiles.put("XOXO")

	# def Quarantine(self):
	# 	orgpath=""
	# 	while(orgpath is not "XOXO"):
	# 		global thread_stop
	# 		if(thread_stop==True):
	# 			break
	# 		orgpath=explicitfiles.get()
	# 		if(orgpath=="XOXO"):
	# 			break
	# 		if(orgpath is not None):
	# 			print(orgpath)
	# 			unique_filename = str(uuid.uuid4())
	# 			chk=filedata.get(unique_filename)
	# 			if(chk is None):
	# 				filedata[unique_filename]=orgpath
	# 				# os.rename(orgpath,"Quarantine/"+unique_filename)
	# 				shutil.copy(orgpath,"Quarantine/"+unique_filename)
	# 			else:
	# 				explicitfiles.put(orgpath)
	# 	with open("data", 'wb') as f:
	# 		pickle.dump(filedata, f, pickle.HIGHEST_PROTOCOL)

	# def Quickie(self):
	# 	thread_stop = False
	# 	t=threading.Thread(target=QuickScan)
	# 	t.start()
	# 	t1=threading.Thread(target=Predict)
	# 	t1.start()
	# 	t2=threading.Thread(target=Quarantine)
	# 	t2.start()

	# def Deepie(self):
	# 	thread_stop = False
	# 	t=threading.Thread(target=Scan)
	# 	t.start()
	# 	t1=threading.Thread(target=Predict)
	# 	t1.start()
	# 	t2=threading.Thread(target=Quarantine)
	# 	t2.start()
