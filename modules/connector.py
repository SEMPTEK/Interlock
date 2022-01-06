from tkinter import *


class PathFrame(Frame):
    frame_configuration = {
        'background': 'green',
    }

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.configure(self.frame_configuration)
        self.label = Label(self, text="Path")
        self.label.pack(side=LEFT)
        self.entry = Entry(self)
        self.entry.pack(side=LEFT)


class NameFrame(Frame):
    frame_configuration = {
        'background': 'blue',
    }

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.label = Label(self, text="Name")
        self.label.pack(side=LEFT)
        self.entry = Entry(self)
        self.entry.pack(side=LEFT)


class Connector(Frame):
    frame_configuration = {
        'background': "white"
    }

    def __init__(self, **kw):
        super().__init__(**kw)
        self.configure(self.frame_configuration)
        self.label_frame = PathFrame(self).pack()
