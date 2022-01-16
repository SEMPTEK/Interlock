"""
This script handles notifications to the user via a bar at the top of the window. This bar always exists, but does not
contain any data until it is activated.
"""

from tkinter import Frame, Label
import session


class NotificationBar(Frame):
    # pack data is read by the window.py script in order to properly build the GUI.
    pack_data = {
        'side': "top",
        'fill': "x",
    }

    frame_configuration = {
        'background': "white",
        'height': 15,
    }

    def clear(self):
        self.label.configure(text="")

    def show_warning(self, text: str):
        self.configure(bg='orange')
        self.label.configure(text=text)

    def show_error(self, text: str):
        self.configure(bg='red')
        self.label.configure(text=text)

    def show(self, text: str):
        self.configure(bg='black')
        self.label.configure(text=text)

    def hide(self):
        self.configure(bg='white')
        self.label.configure(text="")

    def __init__(self, **kw):
        super().__init__(**kw)
        self.configure(self.frame_configuration)
        self.label = Label(self)
        session.notification_manager = self
