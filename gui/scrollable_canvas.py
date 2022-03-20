from tkinter import Scrollbar, Canvas, Frame
from session import winfo


class SubScrollbar(Scrollbar):
    config_data = {
        'background': "white",
        'orient': "vertical",
    }
    pack_data = {
        'side': "left",
        'anchor': 'e',
    }

    def __init__(self, parent, canvas_obj):
        super().__init__(parent)
        self.configure(self.config_data)
        self.configure(command=canvas_obj.yview)
        self.pack(self.pack_data)


class SubCanvas(Canvas):
    canvas_config = {
        'bd': 0,
        'background': "red",
        'width': winfo['width']
    }
    pack_data = {
        'side': "left",
        'expand': True,
    }

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.configure(self.canvas_config)
        self.configure(scrollregion=self.bbox("all"))
        self.pack(self.pack_data)


class ScrollableCanvas(Frame):
    config_data = {
        'background': "white",
    }
    pack_data = {
        'side': "top",
        'anchor': "n",
        'expand': True,
    }

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.canvas = SubCanvas(self)
        self.scrollbar = SubScrollbar(self, self.canvas)
        self.configure(self.config_data)
        self.pack(self.pack_data)
