import requests
from os import path
import subprocess
import shutil

class OpenConference:
    def __init__(self, name):
        self.name = name
        self.URL = None
        self.system_path = None
        self.download_url = None

    def clone_system(self):
        raise NotImplementedError("clone_system method is not implemented yet.")
    
    def open_conference(self):
        raise NotImplementedError("open_conference method is not implemented yet.")
    
    def download(self):
        response = requests.get(self.download_url)
        if response.status_code == 200:
            with open(f"{self.name}_installer.exe", 'wb') as file:
                file.write(response.content)
            print(f"Downloaded {self.name} from {self.download_url}")
        else:
            print(f"Failed to download {self.name} from {self.download_url}")
        
    def install(self):
        print(f"Installing {self.name} from {self.system_path}")
        cmd = f'powershell.exe Start-Process -Wait -FilePath {self.name}_installer.exe -Argument /silent -PassThru'
        returned_value = subprocess.call(cmd, shell=True)
        print(f"Installed end with return value {returned_value}")

    def clone_system(self,id):
        if not path.exists(self.system_path):
            print(f"Cloning {self.name} system to {self.system_path}")
            self.download()
            self.install()
                    
        copy_system_path = path.expandvars(self.system_path+f"{self.name}_{id}.exe")
        if not path.exists(copy_system_path):
            shutil.copy(self.exe_path, copy_system_path)
            print(f"Cloned {self.name} system to {copy_system_path}")      
            
        return copy_system_path  