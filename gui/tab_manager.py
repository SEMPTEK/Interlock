"""
This script manages the navigation of modules via a notebook approach. Each module will display as its own tab.
"""

from tkinter import Frame
from tkinter.ttk import Notebook
from modules import *
import traceback
import session


class TabManager(Notebook):
    pack_data = {
        'side': 'top',
        'fill': 'both',
        'expand': True,
    }

    def load_modules(self):
        for module in module_list:
            try:
                state = "normal"
                if not module_list[module][1]:
                    state = "hidden"
                self.tab_list[module] = module_list[module][0]()
                self.add(self.tab_list[module], text=module, state=state)
            except Exception as e:
                print(e)
                traceback.print_exc()

    def set_active_frame(self, tab_name):
        tab_id = self.tab_list[tab_name]
        self.add(tab_id)
        self.select(tab_id)

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.tab_list = {}
        self.load_modules()
        session.tab_manager = self


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
