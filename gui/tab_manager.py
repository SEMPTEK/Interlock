"""
This script manages the navigation of modules via a notebook approach. Each module will display as its own tab.
"""

from tkinter import Frame
from tkinter.ttk import Notebook
from modules import *
import traceback


class TabManager(Notebook):
    pack_data = {
        'side': 'top',
        'fill': 'both',
        'expand': True,
    }

    def load_modules(self):
        print(module_list)
        for module in module_list:
            try:
                module_object = module_list[module]
                self.add(module_object(), text=module)
            except Exception as e:
                print(e)
                traceback.print_exc()

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.load_modules()


class ModuleFrame(Frame):
    frame_configuration = {
        'borderwidth': 0,
    }

    pack_data = {
        'side': 'left',
        'fill': 'both',
        'expand': True,
    }

    def __init__(self, **kw):
        super().__init__(**kw)
        self.configure(self.frame_configuration)
        self.tab_manager = TabManager(self)
        self.tab_manager.pack(self.tab_manager.pack_data)
