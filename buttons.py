from tkinter import Button
from session import winfo


class ActionButton(Button):
    config_data = {
        'width': winfo['width'],
        'height': 2,
        'background': "white",
        'relief': "groove",
    }
    pack_data = {
        'side': "top",
        'anchor': 'nw',
    }

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.configure(self.config_data)
