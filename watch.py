

#!/usr/bin/python
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
    	if(event.src_path.endswith('.jpg') or event.src_path.endswith('.png') or event.src_path.endswith('.mp4') or event.src_path.endswith('.jpg') or event.src_path.endswith('.bmp') ):
    		print(event.src_path)
        # print(f'event type: {event.event_type}  path : {event.src_path}')


def watch(paths):
    event_handler = MyHandler()
    observer = Observer()
    for i in paths:
	    observer.schedule(event_handler, path=i, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

paths1=['C:\\Users\\Vishals\\Desktop\\','C:\\Users\\Vishals\\Desktop\\UAC\\']
watch(paths1)