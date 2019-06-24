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
import servicemanager
import os
    
cwd = os.path.dirname(os.path.abspath(__file__))
modFiles_log = os.path.join(cwd,"modified_paths.log")
watchDirs = os.path.join(cwd,"watchDirs")

class WatcherMain(FileSystemEventHandler):
    def on_modified(self, event):
        if(event.src_path.endswith('.jpg') or event.src_path.endswith('.png') or event.src_path.endswith('.mp4') or event.src_path.endswith('.flv') or event.src_path.endswith('.jpeg') ):
            g = open(modFiles_log,"r").read()
            if event.src_path not in g:
                f = open(modFiles_log,"a+")
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
        if not os.path.isfile(modFiles_log):
            f = open(modFiles_log,"w+").close()
        event_handler = WatcherMain()
        observer = Observer()
        wD = open(watchDirs,"r")
        for path in wD:
            path = path.rstrip()
            observer.schedule(event_handler, path=path, recursive=True)
        observer.start()
        while self.stop_requested is not True:
            time.sleep(1)
        observer.stop()
        observer.join()
        return
                                                                                                                                                                                                                                                                                                                                                                                                                                    
if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(HelloWorldSvc)