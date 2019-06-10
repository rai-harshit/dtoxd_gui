import os
import threading
# from multiprocessing import Queue
import queue
import tensorflow as tf
tf.logging.set_verbosity(tf.logging.FATAL)
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
import shlex
import subprocess
import re
from numpy.ma import frombuffer

image_data = queue.Queue()
video_data = queue.Queue()
explicitfiles = queue.Queue()
video_frames = queue.Queue()
erroneous_files = queue.Queue()
class Scanner():

	def __init__(self):
		pass

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
								image_data.put(root+"\\"+i)
								total_images_found+=1
						if cs_videos_chkbox:
							if(i.endswith(".mp4") or i.endswith(".mkv") or i.endswith(".avi") or i.endswith(".flv")):
								video_data.put(root+"\\"+i)
								total_videos_found+=1
		if cs_images_chkbox:
			config.scan_details['total_images_found'] = total_images_found
			image_data.put("XOXO")
		if cs_videos_chkbox:
			config.scan_details['tatal_videos_found'] = total_videos_found
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
								image_data.put(os.path.join(root,i))
								# print(root+"/"+i)
								total_images_found+=1
						if cs_videos_chkbox:
							if(i.endswith(".mp4") or i.endswith(".mkv") or i.endswith(".avi") or i.endswith(".flv")):
								video_data.put(os.path.join(root,i))
								# print(root+"/"+i)
								total_videos_found+=1
		if cs_images_chkbox:
			config.scan_details['total_images_found'] = total_images_found
			image_data.put("XOXO")
		if cs_videos_chkbox:
			config.scan_details['tatal_videos_found'] = total_videos_found
			video_data.put("XOXO")

	def FramesExtraction(self,cs_images_chkbox,cs_videos_chkbox,sensitivity_level):
		filename = ""
		while(filename!="XOXO"):
			if(config.thread_stop==True):
				config.scan_details['total_images_scanned'] = config.total_images_scanned
				config.scan_details['total_explicit_images'] = config.total_explicit_images
				explicitfiles_size = explicitfiles.qsize()
				image_queue_size = image_data.qsize()
				video_queue_size = video_data.qsize()
				video_frames_size = video_frames.qsize()
				if(explicitfiles_size > 0):
					for i in range(explicitfiles_size):
						explicitfiles.get()
				if(cs_images_chkbox is True and image_queue_size > 0):
					for i in range(image_queue_size):
						image_data.get()
				if(cs_videos_chkbox is True and video_queue_size > 0):
					for i in range(video_queue_size):
						video_data.get()
				if(cs_videos_chkbox is True and video_frames_size > 0):
					for i in range(video_frames_size):
						video_frames.get()
				break
			filename = video_data.get()
			# print(filename)
			if filename == "XOXO":
				video_frames.put("XOXO")
				break
			video_frames.put("-/-/-/---O---/-/-/-{}".format(filename))
			startupinfo = None
			if os.name == 'nt':
			    startupinfo = subprocess.STARTUPINFO()
			    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW	
			if sensitivity_level==0:
				try:
					base_cmd = 'ffmpeg -hide_banner -i "{}" -ignore_editlist 0 -map 0:v:0 -c copy -f null -'.format(filename)
					vid_info_proc = subprocess.Popen(base_cmd,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,startupinfo=startupinfo)
					vid_info = vid_info_proc.communicate()[0].decode("utf-8")
					# print(vid_info)
					vd = re.findall("time=(.+?) bitrate=",vid_info)[-1].strip().split(":")
				except:
					print("Error occurred while probing video file.")
					erroneous_files.put(filename)
					continue

				time_multiplier = [3600,60,1]
				video_duration = 0
				for i in range(3):
					video_duration+=time_multiplier[i]*float(vd[i])
				# Considering we are extracting 30 frames every video.
				frames_to_ext = 30
				interval = float("%.2f"%(video_duration/frames_to_ext))
				seek_timestamps = []
				for i in range(frames_to_ext):
					seek_timestamps.append((i+1)*interval)
				cmd = 'ffmpeg '
				for c in range(frames_to_ext):
					statement = ' -v quiet -ss {} -i "{}" -vframes 1 -f image2pipe -s 300x300 -map {}:v:0 -pix_fmt bgr24 -vcodec rawvideo - '.format(seek_timestamps[c],filename,c)
					cmd += statement
			else:
				print(filename)
				cmd = 'ffmpeg -v error -skip_frame nokey -i "{}" -vsync vfr -f image2pipe -vcodec rawvideo -pix_fmt bgr24 -s 300x300 - '.format(filename) 

			s1 = subprocess.Popen(cmd, stdout=subprocess.PIPE,stdin=subprocess.DEVNULL,startupinfo=startupinfo)
			while True:
				if(config.thread_stop==True):
					config.scan_details['total_images_scanned'] = config.total_images_scanned
					config.scan_details['total_explicit_images'] = config.total_explicit_images
					explicitfiles_size = explicitfiles.qsize()
					image_queue_size = image_data.qsize()
					video_queue_size = video_data.qsize()
					video_frames_size = video_frames.qsize()
					if(explicitfiles_size > 0):
						for i in range(explicitfiles_size):
							explicitfiles.get()
					if(cs_images_chkbox and image_queue_size > 0):
						for i in range(image_queue_size):
							image_data.get()
					if(cs_videos_chkbox is True and video_queue_size > 0):
						for i in range(video_queue_size):
							video_data.get()
					if(cs_videos_chkbox is True and video_frames_size > 0):
						for i in range(video_frames_size):
							video_frames.get()
					break
				try:
					f = s1.stdout.read(270000)
					frame = frombuffer(f,dtype=np.uint8).reshape((1,300,300,3))
					video_frames.put(frame)
				except ValueError as ve:
					# print(ve)
					break


	def Prediction(self,cs_images_chkbox,cs_videos_chkbox):
		if cs_videos_chkbox:
			explicit_frames_in_video = 0
		clear_session()
		model = load_model("C:\\Users\\g_host\\Desktop\\dtoxd_GUI\\model.h5")
		if cs_images_chkbox:
			x=""
			while(x!="XOXO"):
				if(config.thread_stop==True):
					config.scan_details['total_images_scanned'] = config.total_images_scanned
					config.scan_details['total_explicit_images'] = config.total_explicit_images
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
					# print(x)
					img=cv.imread(x)
					if(img is not None):
						height, width = img.shape[:2]
						if(height>48 and width>48):
							config.statusbar_update.put(x)
							img=cv.resize(img,(300,300))
							img=np.array(img)
							image = np.reshape(img,(1,300,300,3))
							l=model.predict(image)
							config.total_images_scanned+=1
							if(l[0][0]>l[0][1]):
								explicitfiles.put(x)
								config.total_explicit_images+=1
			config.scan_details['total_explicit_images'] = config.total_explicit_images
			config.scan_details['total_images_scanned'] = config.total_images_scanned
			if cs_videos_chkbox is False:
				explicitfiles.put("XOXO")
		if cs_videos_chkbox:
			y = ""
			config.scan_details['total_images_scanned'] = config.total_images_scanned
			config.scan_details['total_explicit_images'] = config.total_explicit_images
			while(y!="XOXO"):
				if(config.thread_stop==True):
					if cs_images_chkbox:
						config.scan_details['total_images_scanned'] = config.total_images_scanned
						config.scan_details['total_explicit_images'] = config.total_explicit_images
					config.scan_details['total_videos_scanned'] = config.total_videos_scanned
					config.scan_details['total_explicit_videos'] = config.total_explicit_videos
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
				y=video_frames.get()
				if type(y)==type("-/-/-/---O---/-/-/-"):
					# print("---------------------------------STRING TYPE MATCH-------------------------")
					videopath = y[19:]
					config.statusbar_update.put(videopath)
					config.total_videos_scanned+=1
					explicit_frames_in_video = 0
					already_pushed = False
				else:
					if explicit_frames_in_video > 10:
						if already_pushed is False:
							explicitfiles.put(videopath)
							already_pushed = True
							config.total_explicit_videos+=1
						else:
							continue
					m=model.predict(y)
					if(m[0][0]>m[0][1]):
						explicit_frames_in_video+=1
			config.scan_details['total_videos_scanned'] = config.total_videos_scanned
			config.scan_details['total_explicit_videos'] = config.total_explicit_videos
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
					# shutil.copy(orgpath,"Quarantine/"+unique_filename)
					# print("File Quarantined : {}".format(orgpath))
				else:
					explicitfiles.put(orgpath)
		with open("data", 'wb') as f:
			pickle.dump(filedata, f, pickle.HIGHEST_PROTOCOL)
