import session
from session import project_manager
from tkinter import Frame, Label, Button, Entry, StringVar

background = "white"


class InputFrame(Frame):
    frame_configuration = {
        'background': background,
    }
    label = Label
    entry = Entry
    pack_data = {
        'side': "top",
        'expand': True,
        'anchor': "w",
    }

    def initialize_label(self, label_text):
        width = 15
        self.label(self, text=label_text)
        self.label.pack(self, side="left", padx=5)

    def initialize_entry(self, entry_text):
        width = 40
        self.entry(self, textvariable=self.data)
        self.entry.pack(self, side="left")
        self.data.set(entry_text)

    def get_entry(self):
        return str(self.data.get())

    def __init__(self, parent, entry_text="", label_text="", **kw):
        super().__init__(parent, **kw)
        self.data = StringVar()
        self.initialize_label(label_text)
        self.initialize_entry(entry_text)


class ProjectEditModule(Frame):
    frame_configuration = {
        'background': "white",
    }
    edit_fields = {
        "Project Name": session.project_manager.active_project.name,
        "Project File Path": session.project_manager.active_project.path,
    }
    input_frame_list = []

    def build_fields(self):
        for field in self.edit_fields:
            frame_obj = InputFrame(self, entry_text="", label_text="Project Name")
            frame_obj.pack(frame_obj.pack_data)
            self.input_frame_list.append(frame_obj)

    def __init__(self, **kw):
        super().__init__(**kw)
        self.active_project = project_manager.active_project
        self.build_fields()
