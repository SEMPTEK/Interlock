from tkinter import Frame, Menu, Menubutton


class FileMenu(Menu):
    menu_configuration = {
        'tearoff': 0,
    }

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.configure(self.menu_configuration)


class EditMenu(Menu):
    menu_configuration = {
        'tearoff': 0,
    }

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.configure(self.menu_configuration)


class ProjectMenu(Menu):
    menu_configuration = {
        'tearoff': 0,
    }

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.configure(self.menu_configuration)


class MenuBar(Menu):
    menu_items = {
        'File': FileMenu,
        'Edit': EditMenu,
        'Project': ProjectMenu,
    }

    def build_menu(self):
        for menu in self.menu_items:
            self.add_cascade(label=menu, menu=self.menu_items[menu](self))

    def __init__(self, **kw):
        super().__init__(**kw)
        self.build_menu()
