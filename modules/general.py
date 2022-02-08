"""
This module is a core module and must exist in order for "Companion" to run. This module contains the settings tab
ase well as all basic features for the software.
"""

from tkinter import Frame, Button, Label

import session


class ViewFilesButton(Button):
    button_config = {
        'background': "white",
        'width': 16,
        'command': session.project_manager.view_project_files,
    }
    pack_data = {
        'side': "left",
        'expand': True,
        'anchor': 'nw',
    }

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.configure(self.button_config)


class GeneralModule(Frame):
    frame_configuration = {
        'background': "white"
    }
    item_list = {
        'View Project Files': ViewFilesButton,
    }

    def load_items(self):
        for item in self.item_list:
            self.item_list[item] = self.item_list[item](self).pack(self.item_list[item].pack_data)

    def __init__(self, **kw):
        super().__init__(**kw)
        self.configure(self.frame_configuration)
        self.load_items()
