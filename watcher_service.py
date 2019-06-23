import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import time
import logging
import random
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import watcher_config

class WatcherMain(FileSystemEventHandler):
    def on_modified(self, event):
        if(event.src_path.endswith('.jpg') or event.src_path.endswith('.png') or event.src_path.endswith('.mp4') or event.src_path.endswith('.flv') or event.src_path.endswith('.jpeg') ):
            g = open("C:\\Users\\g_host\\Desktop\\dtoxd_GUI_dir\\modified_paths.log","r").read()
            if event.src_path not in g:
                f = open("C:\\Users\\g_host\\Desktop\\dtoxd_GUI_dir\\modified_paths.log","a+")
                f.write(event.src_path+"\n")
                f.close()   

class HelloWorldSvc(win32serviceutil.ServiceFramework):
    _svc_name_ = "dtoxd_directory_watcher"
    _svc_display_name_ = "dtoxd Directory Watcher"
    _svc_description_ = "This service is used to monitor particular folders for media files."
    
    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.stop_event = win32event.CreateEvent(None,0,0,None)
        socket.setdefaulttimeout(60)
        self.stop_requested = False

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)
        logging.info('Stopping service ...')
        self.stop_requested = True

    def SvcDoRun(self):
        self.main()

    def main(self):
	    nf = open("C:\\Users\\g_host\\Desktop\\dtoxd_GUI_dir\\modified_paths.log","a+")
	    nf.close()
	    event_handler = WatcherMain()
	    observer = Observer()
	    test = open("C:\\Users\\g_host\\Desktop\\dtoxd_GUI_dir\\test.log","w+")
	    for path in watcher_config.paths:
	    	test.write(path)
	    test.close()
	    for i in watcher_config.paths:
		    observer.schedule(event_handler, path=i, recursive=True)
	    observer.start()
	    while self.stop_requested is not True:
		    time.sleep(1)
	    observer.stop()
	    observer.join()
	    return
                                                                                                                                                                                                                                                                                                                                                                                                                                    
if __name__ == "__main__":
    win32serviceutil.HandleCommandLine(HelloWorldSvc)