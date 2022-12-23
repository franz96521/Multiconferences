import src.screenRecorder.VideoRecorder as VideoRecorder
import src.screenRecorder.AudioRecorder as AudioRecorder

from tkinter import Button, Frame
import subprocess
import time
import threading


class VideoWindow(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        fileName = "recording.mp4"
        path = "."
        self.path = path
        self.fileName = fileName
        self.video_thread = VideoRecorder.VideoRecorder(self)
        self.video_thread.pack()
        self.audio_thread = AudioRecorder.AudioRecorder()

        self.recordBtn = Button(self, text="record", command=self.start)
        self.recordBtn.pack()

        self.stopBtn = Button(self, text="stop", command=self.stop)
        self.stopBtn.pack()

        self.combineBtn = Button(self, text="combine", command=self.combine)
        self.combineBtn.pack()

   

    def start(self):
        print("start recording")
        self.audio_thread.start()
        self.video_thread.start()

    def stop(self):
        print("stop recording")
        self.video_thread.stop()
        self.audio_thread.stop()

    def combine(self):
        while threading.active_count() > 1:
            time.sleep(1)
        cmd = f'"src\\ffmpeg\\ffmpeg.exe" -ac 2 -channel_layout stereo -i "recording.wav" -i "recording.avi" -pix_fmt yuv420p  {self.path}\{self.fileName}.avi'
        subprocess.call(cmd, shell=True)


if __name__ == "__main__":
    window = VideoWindow()
    window.mainloop()

    print("End ")
