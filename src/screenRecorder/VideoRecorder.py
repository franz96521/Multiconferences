from PIL import ImageTk, Image
import threading
from tkinter import Label, Frame
from win32api import GetSystemMetrics
import pyautogui
import cv2
import sys
import numpy as np


class VideoRecorder(Frame):

    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.panel = Label(self, text="video aqui")

        self.output = None
        self.recording = False

        self.panel.pack(padx=10, pady=10)

    def record(self):

        img = pyautogui.screenshot()
        frame = np.array(img)

        if self.panel:

            self.current_image = Image.fromarray(frame)
            self.current_image = self.current_image.resize((480, 272))
            imgtk = ImageTk.PhotoImage(image=self.current_image)

            self.panel.imgtk = imgtk
            self.panel.config(image=imgtk)

        self.output.write(frame)

        if self.recording == True:
            self.after(30, self.record)

    def stop(self):
        self.recording = False
        self.output.release()

    def start(self):
        self.output = cv2.VideoWriter("recording.avi", cv2.VideoWriter_fourcc(
            *"XVID"), 20.0, (GetSystemMetrics(0), GetSystemMetrics(1)))
        self.recording = True
        video_thread = threading.Thread(target=self.record)
        video_thread.start()
