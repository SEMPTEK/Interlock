"""
This is a primary module, which is critical for the software to operate correctly. This module comes included with
the software.
"""

from tkinter import Frame, Button, Label, Listbox
import session


class SelectionBox(Listbox):
    frame_configuration = {
        'background': "white",
        'width': 100,
        'height': 20,
    }
    pack_data = {
        'side': "top",
        'expand': True,
        'anchor': 'n',
    }

    def load_content(self):
        proj_list = session.project_manager.project_list
        for project in proj_list:
            self.insert('end', project)

    def reload(self):
        self.delete(0, 'end')
        self.load_content()

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.configure(self.frame_configuration)
        self.load_content()


class CancelButton(Button):
    frame_configuration = {
        'background': 'white',
        'width': 50,
        'height': 1,
        'text': "Cancel",
    }
    pack_data = {
        'side': "top",
        'expand': True,
        'anchor': "n",
    }

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.configure(self.frame_configuration)


class DeleteButton(Button):
    frame_configuration = {
        'background': "white",
        'width': 50,
        'height': 1,
        'text': "Delete"
    }
    pack_data = {
        'side': "top",
        'expand': True,
        'anchor': 'n',
    }

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.configure(self.frame_configuration)


class RemoveProjectModule(Frame):
    delete_button = DeleteButton
    cancel_button = CancelButton
    selection_box = SelectionBox
    frame_configuration = {
        'background': "white"
    }

    def on_delete(self):
        session.project_manager.remove_project(self.selection_box.get(self.selection_box.curselection()))
        session.navigation_frame.listbox.refresh()
        self.selection_box.reload()

    def on_cancel(self):
        session.tab_manager.reload()
        session.tab_manager.hide(session.tab_manager.tab_list["Remove Projects"])

    def load_items(self):
        self.selection_box = SelectionBox(self)
        self.selection_box.pack(self.selection_box.pack_data)
        self.delete_button = DeleteButton(self, command=self.on_delete)
        self.delete_button.pack(self.delete_button.pack_data)
        self.cancel_button = CancelButton(self, command=self.on_cancel)
        self.cancel_button.pack(self.cancel_button.pack_data)

    def __init__(self, **kw):
        super().__init__(**kw)
        self.configure(self.frame_configuration)
        self.load_items()
