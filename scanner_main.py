import os
import threading
from multiprocessing import Queue
import tensorflow as tf
import keras
from keras.models import load_model
from keras.backend import clear_session
import cv2 as cv
import numpy as np
import logging
import uuid
import pickle
import shutil
import win32api
import time
import config

data = Queue()
explicitfiles = Queue()

class Scanner():

	def __init__(self):
		pass

	# test cases
	# def DeepScan(self):
	# 	dc= 0
	# 	print("Deep Scan Started -- Jaadiye ka Deep Scan wala code.")
	# 	while dc <= 100000000:
	# 		dc+=1
	# 		if config.thread_stop == True:
	# 			break
	# 	print("Deep Scan Completed {}".format(dc))

	# def QuickScan(self):
	# 	print("Quick Scan Started -- Jaadiye ka Quick Scan wala code.")
	# 	qc=0
	# 	while qc <= 50000:
	# 		qc+=1
	# 		if config.thread_stop == True:
	# 			break
	# 	print("Quick Scan Completed {}".format(qc))

	# def Prediction(self):
	# 	print("Prediction Started -- Jaadiye ka Prediction wala code.")
	# 	pc = 0
	# 	while pc <= 250000:
	# 		pc+=1
	# 		if config.thread_stop == True:
	# 			break
	# 	print("Prediction Completed {}".format(pc))

	# def Quarantine(self):
	# 	print("Quarantine Started -- Jaadiye ka Quarantine wala code")
	# 	qarc = 0
	# 	while qarc <= 20405:
	# 		qarc+=1
	# 		if config.thread_stop == True:
	# 			break
	# 	print("Quarantine Completed {}".format(qarc))



	def DeepScan(self):
		drives = win32api.GetLogicalDriveStrings()
		drives = drives.split('\000')[:-1]
		for drive in drives:
			if(config.thread_stop==True):
				data_size = data.qsize()
				for i in range(data_size):
					data.get()
				break
			for (root,dirs,files) in os.walk(drive, topdown=True): 
				if(config.thread_stop==True):
					data_size = data.qsize()
					for i in range(data_size):
						data.get()
					break
				if(len(files)!=0):
					for i in files:
						if(config.thread_stop==True):
							data_size = data.qsize()
							for i in range(data_size):
								data.get()
							break
						if(i.endswith(".jpg") or i.endswith(".png") or i.endswith(".bmp") or i.endswith(".jpeg")):
							data.put(root+"/"+i)
		data.put("XOXO")

	def QuickScan(self):
		total_images_found = 0
		drives = win32api.GetLogicalDriveStrings()
		drives = drives.split('\000')[:-1]
		drives[0]=os.path.expanduser("~")
		# drives = ["C:\\Users\\g_host\\Documents\\"]
		for drive in drives:
			if(config.thread_stop==True):
				config.scan_details['total_images_found'] = total_images_found
				data_size = data.qsize()
				for i in range(data_size):
					data.get()
				break
			for (root,dirs,files) in os.walk(drive, topdown=True):
				if(config.thread_stop==True):
					config.scan_details['total_images_found'] = total_images_found
					data_size = data.qsize()
					for i in range(data_size):
						data.get()
					break
				if(len(files)!=0):
					for i in files:
						if(config.thread_stop==True):
							config.scan_details['total_images_found'] = total_images_found
							data_size = data.qsize()
							for i in range(data_size):
								data.get()
							break
						if(i.endswith(".jpg") or i.endswith(".png") or i.endswith(".bmp") or i.endswith(".jpeg")):
							total_images_found+=1
							data.put(root+"/"+i)
		config.scan_details['total_images_found'] = total_images_found
		data.put("XOXO")

	def Prediction(self):
		total_images_scanned = 0
		total_explicit_images = 0
		clear_session()
		x=""
		model = load_model("model.h5")
		while(x!="XOXO"):
			if(config.thread_stop==True):
				config.scan_details['total_images_scanned'] = total_images_scanned
				config.scan_details['total_explicit_images'] = total_explicit_images
				explicitfiles_size = explicitfiles.qsize()
				for i in range(explicitfiles_size):
					explicitfiles.get()
				data_size = data.qsize()
				for i in range(data_size):
					data.get()
				break
			x=data.get()
			if(x!="" or x is not None):
				img=cv.imread(x)
				if(img is not None):
					height, width = img.shape[:2]
					if(height>48 and width>48):
						config.statusbar_update.put(x)
						img=cv.resize(img,(300,300))
						# img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
						img=np.array(img)
						image = np.reshape(img,(1,300,300,3))
						l=model.predict(image)
						total_images_scanned+=1
						if(l[0][0]>l[0][1]):
							explicitfiles.put(x)
							total_explicit_images+=1
		config.scan_details['total_explicit_images'] = total_explicit_images
		config.scan_details['total_images_scanned'] = total_images_scanned
		explicitfiles.put("XOXO")

	def Quarantine(self):
		filedata = {}
		orgpath=""
		while(orgpath is not "XOXO"):
			if(config.thread_stop==True):
				explicitfiles_size = explicitfiles.qsize()
				for i in range(explicitfiles_size):
					explicitfiles.get()
				break
			orgpath=explicitfiles.get()
			if(orgpath=="XOXO"):
				break
			if(orgpath is not None):
				unique_filename = str(uuid.uuid4())
				chk=filedata.get(unique_filename)
				if(chk is None):
					filedata[unique_filename]=orgpath
					# os.rename(orgpath,"Quarantine/"+unique_filename)
					shutil.copy(orgpath,"Quarantine/"+unique_filename)
				else:
					explicitfiles.put(orgpath)
		with open("data", 'wb') as f:
			pickle.dump(filedata, f, pickle.HIGHEST_PROTOCOL)
		print(explicitfiles.qsize())
