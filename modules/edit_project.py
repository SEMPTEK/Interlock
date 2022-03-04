import session
from session import project_manager
from project_manager import Project
from tkinter import Frame, Label, Button, Entry, StringVar

background = "white"


class InputField(Frame):
    config_data = {
        'background': background,
    }

    def get_entry(self):
        return str(self.entry_data.get())

    def __init__(self, parent, label_text=""):
        super().__init__(parent)
        self.configure(self.config_data)
        self.entry_data = StringVar()
        self.label = Label(self, text=label_text, bg=background)
        self.label.pack(side="left")
        self.entry = Entry(self, bg=background, textvar=self.entry_data)
        self.entry.pack(side="left")


class ProjectEditModule(Frame):
    config_data = {
        'background': background,
    }

    def __init__(self, **kw):
        super().__init__(**kw)
        self.configure(self.config_data)
        self.active_project = project_manager.active_project
        self.name_field = InputField(self, label_text="Name")
        self.name_field.pack(side="top")
        self.path_field = InputField(self, label_text="Path")
        self.path_field.pack(side="top")
        self.enter_button = Button(self)
        self.enter_button.pack(side="top")
        self.cancel_button = Button(self)
        self.cancel_button.pack(side="top")
