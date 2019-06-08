# from multiprocessing import Queue
import queue
thread_stop = False
total_images_scanned = 0
total_videos_scanned = 0
total_explicit_images = 0
total_explicit_videos = 0
scan_details = {}
statusbar_update = queue.Queue()
