#Coordintaor

from PeresntationLayer.window import Window
from PeresntationLayer.Frames.login import LoginFrame
from PeresntationLayer.Frames.register import RegisterFrame
from PeresntationLayer.Frames.home import HomeFrame
from PeresntationLayer.Frames.user_managment import UserManagementFrame


class MainView:
    def __init__(self):
        self.frames = {}  # creating an empty dictionary
        self.window = Window()
        # the last added frame will be shown first
        self.add_frames("user_management", UserManagementFrame(self.window))
        self.add_frames("register", RegisterFrame(self.window, self))
        self.add_frames("home", HomeFrame(self.window, self))
        self.add_frames("Login", LoginFrame(self.window, self))

        self.window.show()

    def add_frames(self, name, frame):
        # adding frames to the dictionary
        self.frames[name] = frame
        frame.grid(row=0, column=0, sticky="nsew")

    def switch_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()
        return frame
