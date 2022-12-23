from tkinter import Label, Frame, StringVar, Button
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import pyvirtualcam
from pyvirtualcam import PixelFormat


class CameraWindow(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.selectedDevice = StringVar()
        self.selectedDevice.trace("w", self.changeCamera)

        self.monthchoosen = ttk.Combobox(
            self, width=27, textvariable=self.selectedDevice)
        self.monthchoosen['values'] = self.list_ports()[1]
        self.monthchoosen.grid(column=0, row=0)

        self.reload = Button(self, text="reiniciar camara",
                             command=self.changeCamera)
        self.reload.grid(column=1, row=0)

        self.vs = self.getCameraCapture()
        self.current_image = None
        self.panel = Label(self)
        self.panel.grid(column=0, row=1, columnspan=2, padx=10, pady=10)
        self.cam = self.getVirtualCam()
        self.video_loop()

    def changeCamera(self, *args):
        self.vs.release()
        self.vs = self.getCameraCapture(device=int(self.selectedDevice.get()))

    def destroy(self):
        super().destroy()
        self.vs.release()
        self.cam.close()

    def getVirtualCam(self, width=1280, height=720, fps_out=30):
        return pyvirtualcam.Camera(
            width, height, fps_out, fmt=PixelFormat.BGR, print_fps=False)

    def getCameraCapture(self, device=0, pref_width=1280, pref_height=720, pref_fps_in=30):
        vc = cv2.VideoCapture(device, cv2.CAP_DSHOW)
        if not vc.isOpened():
            raise RuntimeError('Could not open video source')
        vc.set(cv2.CAP_PROP_FRAME_WIDTH, pref_width)
        vc.set(cv2.CAP_PROP_FRAME_HEIGHT, pref_height)
        vc.set(cv2.CAP_PROP_FPS, pref_fps_in)
        return vc

    def video_loop(self):
        ok, frame = self.vs.read()
        if ok:
            self.cam.send(frame)
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            self.current_image = Image.fromarray(cv2image)
            self.current_image = self.current_image.resize((480, 272))
            imgtk = ImageTk.PhotoImage(image=self.current_image)
            self.panel.imgtk = imgtk
            self.panel.config(image=imgtk)
        self.after(30, self.video_loop)

    def list_ports(self):

        non_working_ports = []
        dev_port = 0
        working_ports = []
        available_ports = []
        while len(non_working_ports) < 6:
            camera = cv2.VideoCapture(dev_port, cv2.CAP_DSHOW)
            if not camera.isOpened():
                non_working_ports.append(dev_port)
                print("Port %s is not working." % dev_port)
            else:
                is_reading, img = camera.read()
                w = camera.get(3)
                h = camera.get(4)
                if is_reading:
                    print("Port %s is working and reads images (%s x %s)" %
                          (dev_port, h, w))
                    working_ports.append(dev_port)
                else:
                    print("Port %s for camera ( %s x %s) is present but does not reads." % (
                        dev_port, h, w))
                    available_ports.append(dev_port)
            dev_port += 1
        return available_ports, working_ports, non_working_ports


if __name__ == "__main__":

    window = CameraWindow()
    window.mainloop()
