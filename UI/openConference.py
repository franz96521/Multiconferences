from tkinter import Button, Label, Frame, Entry
import src.openConference.openTelmex as Telmex
import src.openConference.openZoom as Zoom
import src.openConference.openGoto as goto
import threading


class OpenConferenceWindow(Frame):

    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        self.label = Label(self, text="URL de la conferencia Zoom & Telmex",font=('calibre', 20, 'bold'))
        self.label.pack()

        self.btnOpenAll = Button(
            self, text="abrir Todas ", command=self.openAll)
        self.btnOpenAll.pack()
        self.entrys = []
        for i in range(5):
            self.entrys.append(InputURL(self, i))
            self.entrys[-1].pack()

        self.label = Label(self, text="URL de la conferencia GotoWebinar",font=('calibre', 20, 'bold'))
        self.label.pack()
        for i in range(3):
            self.entrys.append(InputURL(self, i))
            self.entrys[-1].pack()

    def openAll(self):
        for i in self.entrys:
            i.open()


class InputURL(Frame):
    def __init__(self, parent, rowid, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.name = Label(self, text='Nombre', font=('calibre', 10, 'bold'))
        self.name.grid(row=0, column=0)
        self.entryName = Entry(self,)
        self.entryName.grid(row=0, column=1)

        self.url = Label(self, text='Url', font=('calibre', 10, 'bold'))
        self.url.grid(row=0, column=2)
        self.entry = Entry(self)
        self.entry.grid(row=0, column=3)
        self.opnebtn = Button(self, text="abrir", command=self.open)
        self.opnebtn.grid(row=0, column=4)
        self.Systems = [
            ("zoom", Zoom.OpenZoom),
            ("zoom", Telmex.OpenTelmex),
            ("goto", goto.OpenGoToWebinar)

        ]
        self.rowid = rowid

    def open(self):
        url = self.entry.get()
        for s in self.Systems:
            if (s[0] in url):
                print("abriendo ", s[0])
                x = s[1](url, self.rowid)
                t = threading.Thread(target=x.open)
                t.start()
                break


if __name__ == "__main__":
    window = OpenConferenceWindow()
    window.mainloop()

    print("End ")
