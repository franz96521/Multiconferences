from os import path
import subprocess
import threading
import webbrowser 

import time

class OpenGoToWebinar():
    def __init__(self,url,id):
        self.path = '%AppData%\Local\GoToMeeting\\19950\\'
        self.url = url
        self.id = id
        self.name = "g2mcomm"
        self.originalPath = path.expandvars(
            self.path+f"{self.name}.exe").replace("\Roaming", "")
    def open(self):
        o = threading.Thread(target=self.openNew)
        o.start()
        time.sleep(2)
        c = threading.Thread(target=self.openChomeLink)
        c.start()
    

    def openNew(self):
        cmd = self.originalPath
        returned_value = subprocess.call(cmd, shell=True)
    def openChomeLink(self):
        webbrowser.get(using='windows-default').open(self.url,new=2)


if __name__ == "__main__":
    x = OpenGoToWebinar("https://na01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fglobal.gotowebinar.com%2Fjoin%2F6746659850644979541%2F956093613&data=05%7C01%7C%7C0c6d654bcdec40e9ecb108dae47b4cbf%7C84df9e7fe9f640afb435aaaaaaaaaaaa%7C1%7C0%7C638073515470480147%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=MXlx4phXj66yQXMVHlh%2BRsX3HysGpIHr7e%2B4D2kDG94%3D&reserved=0",0)
    t2 = threading.Thread(target=x.open)
    t2.start()
