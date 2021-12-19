"""
The navigation frame is used to select the object of focus (project or other)
"""
from tkinter import Frame, Button, Listbox
import session


class NavListbox(Listbox):
    frame_configuration = {
        'width': 33,
        'borderwidth': 0,
    }
    pack_data = {
        'side': 'left',
        'fill': 'y',
        'padx': 10,
        'pady': 10,
    }

    def load(self):
        pass

    def clear(self):
        pass

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.configure(self.frame_configuration)


class NavFrame(Frame):
    pack_data = {
        'side': "left",
        'fill': "y",
    }

    frame_configuration = {
        'background': "green",
    }

    def __init__(self, **kw):
        super().__init__(**kw)
        self.configure(self.frame_configuration)
        self.listbox = NavListbox(self)
        self.listbox.pack(self.listbox.pack_data)
