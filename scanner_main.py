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

image_data = Queue()
video_data = Queue()
explicitfiles = Queue()
video_frames = Queue()

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



	def DeepScan(self,cs_images_chkbox,cs_videos_chkbox):
		total_images_found = 0
		total_videos_found = 0
		drives = win32api.GetLogicalDriveStrings()
		drives = drives.split('\000')[:-1]
		for drive in drives:
			if(config.thread_stop==True):
				config.scan_details['total_images_found'] = total_images_found
				config.scan_details['total_videos_found'] = total_videos_found
				image_queue_size = image_data.qsize()
				video_queue_size = video_data.qsize()
				if(cs_images_chkbox is True and image_queue_size > 0):
					for i in range(image_queue_size):
						image_data.get()
				if(cs_videos_chkbox is True and video_queue_size > 0):
					for i in range(video_queue_size):
						video_data.get()
				break
			for (root,dirs,files) in os.walk(drive, topdown=True): 
				if(config.thread_stop==True):
					config.scan_details['total_images_found'] = total_images_found
					config.scan_details['total_videos_found'] = total_videos_found
					image_queue_size = image_data.qsize()
					video_queue_size = video_data.qsize()
					if(cs_images_chkbox is True and image_queue_size > 0):
						for i in range(image_queue_size):
							image_data.get()
					if(cs_videos_chkbox is True and video_queue_size > 0):
						for i in range(video_queue_size):
							video_data.get()
					break
				if(len(files)!=0):
					for i in files:
						if(config.thread_stop==True):
							config.scan_details['total_images_found'] = total_images_found
							config.scan_details['total_videos_found'] = total_videos_found
							image_queue_size = image_data.qsize()
							video_queue_size = video_data.qsize()
							if(cs_images_chkbox is True and image_queue_size > 0):
								for i in range(image_queue_size):
									image_data.get()
							if(cs_videos_chkbox is True and video_queue_size > 0):
								for i in range(video_queue_size):
									video_data.get()
							break
						if cs_images_chkbox:
							if(i.endswith(".jpg") or i.endswith(".png") or i.endswith(".bmp") or i.endswith(".jpeg")):
								image_data.put(root+"/"+i)
								# print(root+"/"+i)
								total_images_found+=1
						if cs_videos_chkbox:
							if(i.endswith(".mp4") or i.endswith(".mkv") or i.endswith(".avi") or i.endswith(".flv")):
								video_data.put(root+"/"+i)
								# print(root+"/"+i)
								total_videos_found+=1

		image_data.put("XOXO")
		video_data.put("XOXO")

	def QuickScan(self,cs_images_chkbox,cs_videos_chkbox):
		total_images_found = 0
		total_videos_found = 0
		drives = win32api.GetLogicalDriveStrings()
		drives = drives.split('\000')[:-1]
		drives[0]=os.path.expanduser("~")
		# drives = ["C:\\Users\\g_host\\Documents\\"]
		for drive in drives:
			if(config.thread_stop==True):
				config.scan_details['total_images_found'] = total_images_found
				config.scan_details['total_videos_found'] = total_videos_found
				image_queue_size = image_data.qsize()
				video_queue_size = video_data.qsize()
				if(cs_images_chkbox is True and image_queue_size > 0):
					for i in range(image_queue_size):
						image_data.get()
				if(cs_videos_chkbox is True and video_queue_size > 0):
					for i in range(video_queue_size):
						video_data.get()
				break
			for (root,dirs,files) in os.walk(drive, topdown=True):
				if(config.thread_stop==True):
					config.scan_details['total_images_found'] = total_images_found
					config.scan_details['total_videos_found'] = total_videos_found
					image_queue_size = image_data.qsize()
					video_queue_size = video_data.qsize()
					if(cs_images_chkbox is True and image_queue_size > 0):
						for i in range(image_queue_size):
							image_data.get()
					if(cs_videos_chkbox is True and video_queue_size > 0):
						for i in range(video_queue_size):
							video_data.get()
					break
				if(len(files)!=0):
					for i in files:
						if(config.thread_stop==True):
							config.scan_details['total_images_found'] = total_images_found
							config.scan_details['total_videos_found'] = total_videos_found
							image_queue_size = image_data.qsize()
							video_queue_size = video_data.qsize()
							if(cs_images_chkbox is True and image_queue_size > 0):
								for i in range(image_queue_size):
									image_data.get()
							if(cs_videos_chkbox is True and video_queue_size > 0):
								for i in range(video_queue_size):
									video_data.get()
							break
						if cs_images_chkbox:
							if(i.endswith(".jpg") or i.endswith(".png") or i.endswith(".bmp") or i.endswith(".jpeg")):
								image_data.put(root+"/"+i)
								# print(root+"/"+i)
								total_images_found+=1
						if cs_videos_chkbox:
							if(i.endswith(".mp4") or i.endswith(".mkv") or i.endswith(".avi") or i.endswith(".flv")):
								video_data.put(root+"/"+i)
								# print(root+"/"+i)
								total_videos_found+=1
		config.scan_details['total_images_found'] = total_images_found
		config.scan_details['tatal_videos_found'] = total_videos_found
		image_data.put("XOXO")
		video_data.put("XOXO")

	def FramesExtraction(self,sensitivity_level):
		filename = ""
		if sensitivity_level==0:
			statement = ""
		else:
			statement = ""
		while(filename!="XOXO"):
			if(config.thread_stop==True):
				config.scan_details['total_images_scanned'] = total_images_scanned
				config.scan_details['total_explicit_images'] = total_explicit_images
				explicitfiles_size = explicitfiles.qsize()
				image_queue_size = image_data.qsize()
				video_queue_size = video_data.qsize()
				if(explicitfiles_size > 0):
					for i in range(explicitfiles_size):
						explicitfiles.get()
				if(cs_images_chkbox is True and image_queue_size > 0):
					for i in range(image_queue_size):
						image_data.get()
				if(cs_videos_chkbox is True and video_queue_size > 0):
					for i in range(video_queue_size):
						video_data.get()
				break
			filename = video_data.get()
			# Find some property of every video file using which we can loop over and extract frames.
			# Once you found the propoerty, iterate over it and extract frames till that property is false.
			while("some_condition_about_every_video_file"):
				if(config.thread_stop==True):
					config.scan_details['total_images_scanned'] = total_images_scanned
					config.scan_details['total_explicit_images'] = total_explicit_images
					explicitfiles_size = explicitfiles.qsize()
					image_queue_size = image_data.qsize()
					video_queue_size = video_data.qsize()
					if(explicitfiles_size > 0):
						for i in range(explicitfiles_size):
							explicitfiles.get()
					if(cs_images_chkbox is True and image_queue_size > 0):
						for i in range(image_queue_size):
							image_data.get()
					if(cs_videos_chkbox is True and video_queue_size > 0):
						for i in range(video_queue_size):
							video_data.get()
					break
				
				frame = "some_extraction_statement_here"
				video_frames.put(frame)
			video_frames.put("-/-/-/---O---/-/-/-{}".format(filename))	


	def Prediction(self,cs_images_chkbox,cs_videos_chkbox):
		total_images_scanned = 0
		total_explicit_images = 0
		if cs_videos_chkbox:
			total_videos_scanned = 0
			total_explicit_videos = 0
			explicit_frames_in_video = 0
		clear_session()
		model = load_model("model.h5")
		if cs_images_chkbox:
			x=""
			while(x!="XOXO"):
				if(config.thread_stop==True):
					config.scan_details['total_images_scanned'] = total_images_scanned
					config.scan_details['total_explicit_images'] = total_explicit_images
					# config.scan_details['total_videos_scanned'] = total_videos_scanned
					# config.scan_details['total_explicit_videos'] = total_explicit_videos
					explicitfiles_size = explicitfiles.qsize()
					image_queue_size = image_data.qsize()
					video_queue_size = video_data.qsize()
					if(explicitfiles_size > 0):
						for i in range(explicitfiles_size):
							explicitfiles.get()
					if(cs_images_chkbox is True and image_queue_size > 0):
						for i in range(image_queue_size):
							image_data.get()
					if(cs_videos_chkbox is True and video_queue_size > 0):
						for i in range(video_queue_size):
							video_data.get()
					break
				x=image_data.get()
				if(x!="" or x is not None):
					img=cv.imread(x)
					if(img is not None):
						height, width = img.shape[:2]
						if(height>48 and width>48):
							config.statusbar_update.put(x)
							img=cv.resize(img,(300,300))
							img=np.array(img)
							image = np.reshape(img,(1,300,300,3))
							l=model.predict(image)
							total_images_scanned+=1
							if(l[0][0]>l[0][1]):
								explicitfiles.put(x)
								total_explicit_images+=1
			config.scan_details['total_explicit_images'] = total_explicit_images
			config.scan_details['total_images_scanned'] = total_images_scanned
			if cs_videos_chkbox is False:
				explicitfiles.put("XOXO")
		if cs_videos_chkbox:
			y = ""
			while(y!="XOXO"):
				if(config.thread_stop==True):
					config.scan_details['total_images_scanned'] = total_images_scanned
					config.scan_details['total_explicit_images'] = total_explicit_images
					config.scan_details['total_videos_scanned'] = total_videos_scanned
					config.scan_details['total_explicit_videos'] = total_explicit_videos
					explicitfiles_size = explicitfiles.qsize()
					image_queue_size = image_data.qsize()
					video_queue_size = video_data.qsize()
					frames_queue_size = video_frames.qsize()
					if(explicitfiles_size > 0):
						for i in range(explicitfiles_size):
							explicitfiles.get()
					if(cs_images_chkbox is True and image_queue_size > 0):
						for i in range(image_queue_size):
							image_data.get()
					if(cs_videos_chkbox is True and video_queue_size > 0):
						for i in range(video_queue_size):
							video_data.get()
						if(frames_queue_size > 0):
							for j in range(frames_queue_size):
								video_frames.get()
					break
				if "-/-/-/---O---/-/-/-" in y:
					videopath = y[19:]
					total_videos_scanned+=1
					if explicit_frames_in_video > 10:
						explicitfiles.put(videopath)
					explicit_frames_in_video = 0
				y=video_frames.get()
				m=model.predict(y)
				if(m[0][0]>m[0][1]):
					explicit_frames_in_video+=1
			config.scan_details['total_videos_scanned'] = total_videos_scanned
			config.scan_details['total_explicit_videos'] = total_explicit_videos
			explicitfiles.put("XOXO")

	def Quarantine(self):
		filedata = {}
		orgpath=""
		while(orgpath is not "XOXO"):
			if(config.thread_stop==True):
				explicitfiles_size = explicitfiles.qsize()
				if explicitfiles_size > 0:
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
