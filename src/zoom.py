from os import path,getenv
import subprocess
import shutil
from  src.openConference import OpenConference

class Zoom(OpenConference):
    def __init__(self):
        super().__init__("Zoom")        
        self.system_path = f'{getenv("APPDATA")}\Zoom\\bin\\'
        self.download_url = 'https://zoom.us/client/latest/ZoomInstaller.exe?archType=x64'
        self.exe_path = path.expandvars(self.system_path+f"{self.name}.exe")

    def clone_system(self,id):
        if not path.exists(self.system_path):
            print(self.system_path)
            print(f"Installing {self.name} system to {self.system_path}")
            self.download()
            self.install()
                    
        copy_system_path = path.expandvars(self.system_path+f"{self.name}_{id}.exe")
        if not path.exists(copy_system_path):
            shutil.copy(self.exe_path, copy_system_path)
            print(f"Cloned {self.name} system to {copy_system_path}")      
            
        return copy_system_path  
        
    def open_conference(self,url,id):
        print(f"Opening {self.name} for {url} with id {id}")
        system_path = self.clone_system(id)
        cmd = f'{system_path} --url={url}'
        subprocess.call(cmd, shell=True)
       