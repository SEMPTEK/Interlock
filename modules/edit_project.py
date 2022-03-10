import session
from session import project_manager
from project_manager import Project
from tkinter import Frame, Label, Button, Entry, StringVar

background = "white"


class InputField(Frame):
    config_data = {
        'background': background,
    }
    input_config = {
        'width': 50,
    }
    label_config = {
        'width': 20,
    }

    def get_entry(self):
        return str(self.entry_data.get())

    def set_entry(self, text: str):
        self.entry_data.set(text)

    def __init__(self, parent, label_text="", entry_text=""):
        super().__init__(parent)
        self.configure(self.config_data)
        self.entry_data = StringVar()
        self.label = Label(self, text=label_text, bg=background)
        self.label.config(self.label_config)
        self.label.pack(side="left", anchor="e")
        self.entry = Entry(self, bg=background, textvariable=self.entry_data)
        self.entry.configure(self.input_config)
        self.entry.pack(side="left")
        self.set_entry(entry_text)


class ProjectEditModule(Frame):
    config_data = {
        'background': background,
    }
    button_config = {
        'width': session.winfo["width"],
        'height': 2,
        'relief': "groove",
        'background': "white",
    }

    def __on_enter(self):
        session.project_manager.update_active_project(self.name_field.get_entry(), self.path_field.get_entry())
        session.tab_manager.reload()

    def __on_reset(self):
        self.name_field.set_entry(self.active_project.name)
        self.path_field.set_entry(self.active_project.path)

    def __on_cancel(self):
        self.__on_reset()
        session.tab_manager.reload()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.configure(self.config_data)
        self.active_project = project_manager.active_project
        self.name_field = InputField(self, label_text="Name", entry_text=str(self.active_project.name))
        self.name_field.pack(side="top", anchor="w")
        self.path_field = InputField(self, label_text="Path", entry_text=str(self.active_project.path))
        self.path_field.pack(side="top", anchor="w")
        self.enter_button = Button(self, text="Save", command=self.__on_enter)
        self.enter_button.configure(self.button_config)
        self.enter_button.pack(side="top")
        self.reset_button = Button(self, text="Reset", command=self.__on_reset)
        self.reset_button.configure(self.button_config)
        self.reset_button.pack(side="top")
        self.cancel_button = Button(self, text="Cancel", command=self.__on_cancel)
        self.cancel_button.configure(self.button_config)
        self.cancel_button.pack(side="top")
