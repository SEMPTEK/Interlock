"""
The navigation frame is used to select the object of focus (project or other)
"""
from tkinter import Frame, Listbox
import session


class NavListbox(Listbox):
    frame_configuration = {
        'width': 33,
        'borderwidth': 0,
    }
    pack_data = {
        'side': 'left',
        'fill': 'y',
        'padx': 10,
        'pady': (0, 10),
    }

    def load(self):
        proj_list = session.project_manager.project_list
        for proj in proj_list:
            self.insert('end', proj)
            print(f"Found {proj}")

    def clear(self):
        self.delete(0, -1)

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.configure(self.frame_configuration)
        self.load()


class NavFrame(Frame):
    pack_data = {
        'side': "left",
        'fill': "y",
    }

    frame_configuration = {
        'background': "white",
    }

    def __init__(self, **kw):
        super().__init__(**kw)
        self.configure(self.frame_configuration)
        self.listbox = NavListbox(self)
        self.listbox.pack(self.listbox.pack_data)
