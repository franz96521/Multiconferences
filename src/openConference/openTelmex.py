from os import path
import subprocess
import src.openConference.CheckExist as CheckExist
import shutil


class OpenTelmex():
    def __init__(self, url, id):
        self.url = url
        self.id = id
        self.path = '%APPDATA%\Videoconferencia Telmex\\bin\\'
        self.download = 'https://videoconferencia.telmex.com/client/latest/VideoconferenciaTelmex.exe'
        self.name = "VideoconferenciaTelmex"
        self.exePath = path.expandvars(f'{self.path}{self.name}_{self.id}.exe')
        self.originalPath = path.expandvars(f'{self.path}{self.name}.exe')

    def open(self):
        telmexCheck = CheckExist.checkIfInstall(
            self.name, self.originalPath, self.download)
        telmexCheck.installIfNotExist()
        self.copyFile()
        self.openConference()

    def copyFile(self):

        if not path.exists(self.exePath):
            print("copiando")
            print(self.exePath)
            print(self.originalPath)
            shutil.copy(self.originalPath, self.exePath)

    def openConference(self):
        cmd = f'"{self.exePath}" --url={self.url}'
        returned_value = subprocess.call(cmd, shell=True)


if __name__ == "__main__":
    x = OpenTelmex(
        "https://us04web.telmex.us/j/73847349176?pwd=S6CpIyt2bYkG2wVVcWNWBdpIfnlaaL.1", 0)
    x.open()
