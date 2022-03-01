"""
This module is a core module and must exist in order for "Interlock" to run. This module contains the settings tab
ase well as all basic features for the software.
"""

from tkinter import Frame
from buttons import ActionButton
import session

command_list = {
    'Open Project Files': {
        'command': session.project_manager.view_project_files,
        'text': "Open Project Files",
    },
    'Edit Project Data': {
        'command': session.project_manager.edit_project_data,
        'text': "Edit Project Data",
    },
}


class GeneralModule(Frame):
    frame_configuration = {
        'background': "white"
    }
    item_list = {}

    def load_items(self):
        global command_list
        for action in command_list:
            action_exec = command_list[action]
            self.item_list[action] = ActionButton(self)
            self.item_list[action].configure(command_list[action])
            self.item_list[action].pack(self.item_list[action].pack_data)

    def __init__(self, **kw):
        super().__init__(**kw)
        self.configure(self.frame_configuration)
        self.load_items()
