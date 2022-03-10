"""
This module is a core module and must exist in order for "Interlock" to run. This module contains the settings tab
ase well as all basic features for the software.
"""

from tkinter import Frame, Tk
from buttons import ActionButton
import session


def do_nothing():
    pass


command_list = {
    'Open Project Files': {
        'command': session.project_manager.view_project_files,
        'text': "Open Project Files",
    },
    'Manage Modules': {
        'command': do_nothing,
        'text': "Manage Modules",
    }
}


class GeneralModule(Frame):
    frame_configuration = {
        'background': "white"
    }
    item_list = {}
    button_config = {
        'width': session.winfo["width"],
        'height': 2,
        'relief': "groove",
    }
    button_pack_data = {
        'side': "top",
        'anchor': "w",
    }

    def load_items(self):
        global command_list
        for action in command_list:
            self.item_list[action] = ActionButton(self)
            self.item_list[action].configure(command_list[action])
            self.item_list[action].configure(self.button_config)
            self.item_list[action].pack(self.button_pack_data)

    def __init__(self, **kw):
        super().__init__(**kw)
        self.configure(self.frame_configuration)
        self.load_items()
