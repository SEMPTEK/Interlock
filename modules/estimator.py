# TODO: build module for estimating project costs based on sheet count, tonnage, etc...

from tkinter import Frame, Button, Label


class EstimatorModule(Frame):
    frame_configuration = {
        'background': "white"
    }

    def __init__(self, **kw):
        super().__init__(**kw)
        self.configure(self.frame_configuration)
