"""
This script manages the navigation of modules via a notebook approach. Each module will display as its own tab.
"""

from tkinter import Frame
from tkinter.ttk import Notebook

module_list = {
    'general'
}


class TabManager(Notebook):
    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)


class ModuleFrame(Frame):
    frame_configuration = {
        'bg': 'blue',
    }

    pack_data = {
        'side': 'left',
        'fill': 'both',
        'expand': True,
    }

    def load_modules(self):
        pass

    def __init__(self, **kw):
        super().__init__(**kw)
        self.configure(self.frame_configuration)
        self.tab_manager = TabManager(self)
