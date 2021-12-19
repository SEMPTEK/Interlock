"""
This module is a core module and must exist in order for "Companion" to run. This module contains the settings tab
ase well as all basic features for the software.
"""

from tkinter import Frame, Button, Listbox


class ProjectTrackerModule(Frame):
    frame_configuration = {
        'background': "white"
    }

    def __init__(self, **kw):
        super().__init__(**kw)
        self.configure(self.frame_configuration)
