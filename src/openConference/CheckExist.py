import sys
import requests
from os import path
import subprocess


class checkIfInstall():
    def __init__(self, name, path, URL):
        self.path = path
        self.URL = URL
        self.name = name

    def installIfNotExist(self):
        if (not self.checkPathExist()):
            self.download()
            self.install()

    def checkPathExist(self):

        print(path.exists(self.path), self.path)
        return path.exists(self.path)

    def download(self):
        response = requests.get(self.URL)
        open(self.name+".exe", "wb").write(response.content)

    def install(self):
        cmd = f'powershell.exe Start-Process -Wait -FilePath {self.name}.exe -Argument /silent -PassThru'

        returned_value = subprocess.call(cmd, shell=True)


if __name__ == "__main__":
    telmex = ("telmex", '%APPDATA%\Videoconferencia Telmex\\bin\VideoconferenciaTelmex.exe',
              'https://videoconferencia.telmex.com/client/latest/VideoconferenciaTelmex.exe')
    zoom = ("zoom", '%APPDATA%\Zoom\\bin\zoom.exe',
            'https://zoom.us/client/latest/ZoomInstaller.exe?archType=x64')

    checkTelmex = checkIfInstall(telmex[0], telmex[1], telmex[2])
    checkTelmex.installIfNotExist()
    checkZoom = checkIfInstall(zoom[0], zoom[1], zoom[2])
    checkZoom.installIfNotExist()
