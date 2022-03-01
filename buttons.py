from tkinter import Button


class ActionButton(Button):
    config_data = {
        'width': 16,
        'background': "white",
    }
    pack_data = {
        'side': "left",
        'expand': True,
        'anchor': 'nw',
    }

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.configure(self.config_data)
