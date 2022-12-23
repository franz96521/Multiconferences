from tkinter import Tk
from tkinter import *
import src.camera.cameraModule as camera
import src.screenRecorder.recordScreen as recordScreen
import UI.openConference as openConference

from tkinter.ttk import Notebook


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi Conferencias")

        photo = PhotoImage(file = "img/logo.png")
        self.iconphoto(False, photo)
        self.tabsystem = Notebook(self)
        self.tab1 = Frame(self.tabsystem)
        self.tab2 = Frame(self.tabsystem)
        self.tab3 = Frame(self.tabsystem)

        self.tabsystem.add(self.tab1, text='Camara')
        self.tabsystem.add(self.tab2, text='grabar pantalla')
        self.tabsystem.add(self.tab3, text='abrir Conferencias')
        self.tabsystem.pack(expand=1, fill="both")

        self.cameraWindow = camera.CameraWindow(self.tab1)

        self.cameraWindow.grid(column=1,
                               row=1,
                               padx=40,
                               pady=40)

        self.screenRecordereWindow = recordScreen.VideoWindow(self.tab2)
        self.screenRecordereWindow.grid(column=1,
                                        row=1,
                                        padx=40,
                                        pady=40)

        self.openConferenceWindow = openConference.OpenConferenceWindow(self.tab3)
        self.openConferenceWindow.grid(column=1,
                                       row=1,
                                       padx=40,
                                       pady=40)


if __name__ == "__main__":

    # Start the event loop.
    window = Window()
    window.mainloop()
