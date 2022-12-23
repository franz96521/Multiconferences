from os import path
import subprocess
import src.openConference.CheckExist as CheckExist
import shutil


class OpenZoom():
    def __init__(self, url, id):
        self.url = url
        self.id = id
        self.path = '%APPDATA%\Zoom\\bin\\'
        self.download = 'https://zoom.us/client/latest/ZoomInstaller.exe?archType=x64'
        self.name = "zoom"
        self.exePath = path.expandvars(self.path+f"{self.name}_{self.id}.exe")
        self.originalPath = path.expandvars(self.path+f"{self.name}.exe")

    def open(self):
        zoomCheck = CheckExist.checkIfInstall(
            self.name, self.originalPath, self.download)
        zoomCheck.installIfNotExist()
        self.copyFile()
        self.openConference()

    def copyFile(self):

        if not path.exists(self.exePath):
            print("copiando")
            shutil.copy(self.originalPath, self.exePath)

    def openConference(self):
        cmd = f'{self.exePath} --url={self.url}'
        returned_value = subprocess.call(cmd, shell=True)


if __name__ == "__main__":
    x = OpenZoom(
        "https://us04web.zoom.us/j/73847349176?pwd=S6CpIyt2bYkG2wVVcWNWBdpIfnlaaL.1", 3)
    x.open()
