from tkinter import *
import session


class InputField(Frame):
    frame_configuration = {
        'background': "white",
    }
    pack_data = {
        'side': TOP,
        'expand': False,
        'anchor': W,
    }

    def __init__(self, parent, label_text="", **kw):
        super().__init__(parent, **kw)
        self.entry_data = StringVar()
        self.label = Label(self, text=label_text, width=10, bg="white")
        self.label.pack(side=LEFT, padx=10, anchor=E)
        self.entry = Entry(self, textvariable=self.entry_data, width=80, bg="white")
        self.entry.pack(side=LEFT, padx=10)
        self.configure(self.frame_configuration)


class ActionButtons(Frame):
    add_project = Button
    reset = Button
    cancel = Button
    frame_configuration = {
        'background': "white",
    }
    pack_data = {
        'side': TOP,
        'expand': False,
    }

    def on_add(self):
        self.parent.send_data()

    def on_reset(self):
        self.parent.reset()

    def on_cancel(self):
        self.parent.cancel()

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.parent = parent
        self.add_project(self, text="Add Project", command=self.on_add).pack(side=TOP)
        self.reset(self, text="Reset", command=self.on_reset).pack(side=TOP)
        self.cancel(self, text="Cancel", command=self.on_cancel).pack(side=TOP)


class Connector(Frame):
    frame_configuration = {
        'background': "white",
    }
    button_frame = ActionButtons

    def build_frames(self):
        self.active_frames['Name'] = InputField(self, label_text="Name")
        self.active_frames['Path'] = InputField(self, label_text="Path")
        for frame in self.active_frames:
            self.active_frames[frame].pack(self.active_frames[frame].pack_data)

    def build_buttons(self):
        self.button_frame(self).pack(self.button_frame.pack_data)

    def send_data(self):
        name = str(self.active_frames['Name'].entry_data.get())
        print(name)
        path = str(self.active_frames['Path'].entry_data.get())
        print(path)
        session.project_manager.add_project(name, path)
        session.tab_manager.hide(session.tab_manager.tab_list["Add Project"])

    def cancel(self):
        self.reset()
        session.tab_manager.hide(session.tab_manager.tab_list["Add Project"])

    def reset(self):
        for frame in self.active_frames:
            self.active_frames[frame].entry_data.set("")

    def __init__(self, **kw):
        super().__init__(**kw)
        self.configure(self.frame_configuration)
        self.active_frames = {}
        self.build_frames()
        self.build_buttons()
