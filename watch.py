

#!/usr/bin/python
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import watcher_config

class WatcherMain(FileSystemEventHandler):
    def on_modified(self, event):
        if(event.src_path.endswith('.jpg') or event.src_path.endswith('.png') or event.src_path.endswith('.mp4') or event.src_path.endswith('.flv') or event.src_path.endswith('.jpeg') ):
            g = open("modified_paths.log","r").read()
            if event.src_path not in g:
                print("New File Found. Writing it to the log.")
                f = open("modified_paths.log","a+")
                f.write(event.src_path+"\n")
                f.close()           

class ReportUpdater(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == "C:\\Users\\g_host\\Desktop\\dtoxd_GUI_dir\\modified_paths.log":
            watcher_config.report_update_available = True
            # print("Report Update Available")

def start_watching(paths):
    print("Start Watching")
    if len(paths) == 0:
        return
    event_handler = WatcherMain()
    observer = Observer()
    for i in paths:
	    observer.schedule(event_handler, path=i, recursive=True)
    observer.start()
    while watcher_config.stop_watcher is not True:
        time.sleep(1)
    observer.stop()
    observer.join()

def report_updater(path):
    print("Started Reporting")
    event_handler = ReportUpdater()
    observer = Observer()
    observer.schedule(event_handler,path=path)
    observer.start()
    while watcher_config.stop_watcher is not True:
        time.sleep(1)
    observer.stop()
    observer.join()


""" TRACKING MODIFICATIONS TO THE modified_paths.log file. """

# paths1=['C:\\Users\\g_host\\Downloads\\',"C:\\Users\\g_host\\Desktop\\dtoxd_GUI_dir"]
# start_watching(paths1)