"""
This script manages the navigation of modules via a notebook approach. Each module will display as its own tab.
"""

from tkinter import Frame
from tkinter.ttk import Notebook


class ModuleFrame(Frame):
    frame_configuration = {
        'bg': 'blue',
    }

    pack_data = {
        'side': 'left',
        'fill': 'both',
        'expand': True,
    }

    def __init__(self, **kw):
        super().__init__(**kw)
        self.configure(self.frame_configuration)


class TabManager(Notebook):
    def __init__(self, **kw):
        super().__init__(**kw)
