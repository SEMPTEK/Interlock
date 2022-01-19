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
        self.label.configure(text="", bg='white')

    def show_warning(self, text: str):
        self.configure(bg='orange')
        self.label.configure(text=text, bg='orange')

    def show_error(self, text: str):
        self.configure(bg='red')
        self.label.configure(text=text, bg='red')

    def show(self, text: str):
        self.configure(bg='white')
        self.label.configure(text=text, bg='white')

    def hide(self):
        self.configure(bg='white')
        self.label.configure(text="", bg='white')

    def __init__(self, **kw):
        super().__init__(**kw)
        self.configure(self.frame_configuration)
        self.label = Label(self, bg='white')
        self.label.pack()
        session.notification_manager = self
