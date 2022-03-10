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
                state = module_list[module][1]
                self.tab_list[module] = module_list[module][0]()
                self.add(self.tab_list[module], text=module)
                if not state:
                    self.hide(self.tab_list[module])
            except Exception as e:
                print(e)
                traceback.print_exc()

    def set_active_frame(self, tab_name, lock_others=False):
        self.reload()
        tab_id = self.tab_list[tab_name]
        if lock_others:
            for tab in self.tab_list:
                self.hide(self.tab_list[tab])
                pass
        self.add(tab_id)
        self.select(tab_id)

    def reload(self):
        for tab in self.tab_list:
            self.hide(self.tab_list[tab])
        self.load_modules()

    def enable(self):
        self.reload()

    def disable(self):
        for tab in self.tab_list:
            self.hide(self.tab_list[tab])

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.tab_list = {}
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
