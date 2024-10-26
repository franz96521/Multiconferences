from os import path,getenv
import subprocess

from  src.openConference import OpenConference
import os 

import subprocess
import threading
import webbrowser 

import time

class GoTo(OpenConference):
    def __init__(self):
        super().__init__("g2mcomm")                
        appdata= getenv("APPDATA").replace("\Roaming", "")
        system_path = f'{appdata}\\Local\GoToMeeting\\'
        folders = [f for f in os.listdir(system_path) if path.isdir(path.join(system_path, f))]
        self.system_path = f'{system_path}{folders[0]}\\'
        self.exe_path = path.expandvars(self.system_path+f"{self.name}.exe")
      
    def open_goto(self):
        cmd = path.expandvars(self.system_path+f"{self.name}.exe")
        subprocess.call(cmd, shell=True)
        
    def open_chrome(self,url,id):
        webbrowser.get(using='windows-default').open(url,new=2)
        
    def open_conference(self,url,id):
        o = threading.Thread(target=self.open_goto)
        o.start()
        time.sleep(2)
        c = threading.Thread(target=self.open_chrome, args=[url,id])
        c.start()
