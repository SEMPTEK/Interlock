from tkinter import Menu
import session
import file_manager

def doNothing():
    print('pong')


class FileMenu(Menu):
    menu_configuration = {
        'tearoff': 0,
    }
    menu_commands = {
        'Open Project Folder': lambda: session.project_manager.view_project_files(),
    }

    def load_commands(self):
        for com in self.menu_commands:
            self.add_command(label=com, command=self.menu_commands[com])

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.configure(self.menu_configuration)
        self.load_commands()


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

    menu_commands = {
        'Link Project': lambda: session.tab_manager.set_active_frame("Add Project", True),
        'Remove Project': lambda: session.tab_manager.set_active_frame("Remove Projects", True),
    }

    def load_commands(self):
        for com in self.menu_commands:
            self.add_command(label=com, command=self.menu_commands[com])

    def __init__(self, parent, **kw):
        super().__init__(parent, **kw)
        self.parent = parent
        self.configure(self.menu_configuration)
        self.load_commands()


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
