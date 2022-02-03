from tkinter import *
from tkinter import filedialog
import session


class InputField(Frame):
    frame_configuration = {
        'background': "white",
    }
    pack_data = {
        'side': TOP,
        'anchor': W,
        'pady': 5,
    }

    def get_from_explorer(self):
        self.entry_data.set(filedialog.askdirectory(initialdir="/", title="Link Project Path"))

    def __init__(self, parent, label_text="", **kw):
        super().__init__(parent, **kw)
        self.entry_data = StringVar()
        self.label = Label(self, text=label_text, width=10, bg="white")
        self.label.pack(side=LEFT, padx=10, anchor=E)
        self.entry = Entry(self, textvariable=self.entry_data, width=100, bg="white")
        self.entry.pack(side=LEFT, padx=5)
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
        'anchor': NW,
    }
    button_pack_data = {
        'side': TOP,
        'pady': 5,
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
        self.configure(self.frame_configuration)
        self.add_project(self, text="Add Project", width=110, background="ghost white",
                         command=self.on_add, relief="flat").pack(self.button_pack_data)
        self.reset(self, text="Reset", width=110, background="ghost white",
                   command=self.on_reset, relief="flat").pack(self.button_pack_data)
        self.cancel(self, text="Cancel", width=110, background="ghost white",
                    command=self.on_cancel, relief="flat").pack(self.button_pack_data)


class AddProjectFrame(Frame):
    frame_configuration = {
        'background': "white",
    }
    button_frame = ActionButtons

    def build_frames(self):
        self.active_frames['Name'] = InputField(self, label_text="Name")
        self.active_frames['Path'] = InputField(self, label_text="Path")
        for frame in self.active_frames:
            self.active_frames[frame].pack(self.active_frames[frame].pack_data)

    def set_binds(self):
        self.active_frames['Path'].entry.bind("<Double-Button-1>",
                                              lambda _: self.active_frames['Path'].get_from_explorer())

    def build_buttons(self):
        self.button_frame(self).pack(self.button_frame.pack_data)

    def send_data(self):
        name = str(self.active_frames['Name'].entry_data.get())
        print(name)
        path = str(self.active_frames['Path'].entry_data.get())
        print(path)
        session.project_manager.add_project(name, path)
        session.tab_manager.reload()
        session.tab_manager.hide(session.tab_manager.tab_list["Add Project"])

    def cancel(self):
        self.reset()
        session.tab_manager.reload()
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
        self.set_binds()
