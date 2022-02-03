"""
The navigation frame is used to select the object of focus (project or other)
"""
from tkinter import Frame, Listbox, END
import session


class NavListbox(Listbox):
    frame_configuration = {
        'width': 33,
        'borderwidth': 1,
        'highlightthickness': 0,
        'selectforeground': 'white',
        'selectbackground': 'orange',
        'activestyle': "none",
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
        self.delete(0, END)

    def refresh(self):
        self.clear()
        self.load()

    def send_active_project_request(self):
        try:
            selection_data = self.get(self.curselection())
            session.project_manager.set_active_project(selection_data)
        except Exception as e:
            session.notification_manager.show_error(f"Error: {e}")

    def load_bindings(self):
        self.bind("<Double-Button-1>", lambda _: self.send_active_project_request())
        self.bind("<Return>", lambda _: session.project_manager.set_active_project(self.get(
            self.curselection())))

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.configure(self.frame_configuration)
        self.load()
        self.load_bindings()


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
        session.navigation_frame = self
