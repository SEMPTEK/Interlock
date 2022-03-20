"""
This module is a core module and must exist in order for "Companion" to run. This module contains the settings tab
ase well as all basic features for the software.
"""

from tkinter import Frame
from buttons import ActionButton
from gui.scrollable_canvas import ScrollableCanvas


class AddRFIButton(ActionButton):
    button_config = {
        'text': "Add",
        'command': lambda: print("Test2"),
    }

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.configure(self.button_config)
        self.pack(self.pack_data)


class RemoveRFIButton(ActionButton):
    button_config = {
        'text': "Delete",
        'command': lambda: print("TEST"),
    }

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.configure(self.button_config)
        self.pack(self.pack_data)


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

    def __init__(self, **kw):
        super().__init__(**kw)
        self.configure(self.frame_configuration)
        self.rfi_canvas = ScrollableCanvas(self)
        self.add_rfi_button = AddRFIButton(self)
        self.remove_rfi_button = RemoveRFIButton(self)
