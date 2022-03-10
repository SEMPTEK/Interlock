"""
This module is a core module and must exist in order for "Companion" to run. This module contains the settings tab
ase well as all basic features for the software.
"""

from tkinter import Frame, Button, Canvas
import file_manager


class RFICanvas(Canvas):
    canvas_config = {
        'bd': 0,
        'background': "white",
    }
    pack_data = {
        'side': "top",
        'anchor': "w",
        'expand': True,
    }

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)


class AddButton(Button):
    button_config = {

    }
    pack_data = {

    }

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)


class RFIFrame(Frame):
    frame_config = {
        'background': "white",
        'height': 20,
        'width': 500,
    }
    pack_data = {
        'side': "top",
        'anchor': "w",
    }

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)


class RFIManagerModule(Frame):
    frame_configuration = {
        'background': "white"
    }
    rfi_list = {}

    def get_rfi_list(self):
        rfi_list = file_manager.read_local()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.configure(self.frame_configuration)
        self.scrollbox = RFICanvas(self)
        self.scrollbox.pack(self.scrollbox.pack_data)
