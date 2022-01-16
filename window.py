from tkinter import Tk
import session
import gui


class Window(Tk):
    config_data = {
        'background': "white",
    }
    name = session.name
    window_size = "860x540"
    min_height = 540
    min_width = 860
    frame_list = {
        'notification_bar': gui.notification_bar.NotificationBar,
        'navigation_box': gui.navigation.NavFrame,
        'tab_frame': gui.tab_manager.ModuleFrame,
    }

    def layout(self):
        for frame in self.frame_list:
            frame_object = self.frame_list[frame]()
            frame_object.pack(frame_object.pack_data)

    def __init__(self):
        super().__init__()
        # use inherited function "configuration()" to configure window using var "config_data" above
        self.configure(self.config_data)
        # use inherited function "title()" to set title using setting var "name" above
        self.title(self.name)
        # use inherited function "geometry()" to set height and width using var "window_size" above
        self.geometry(self.window_size)
        # use inherited function minsize() to set minimum window size using var "min_window_size" above
        self.minsize(self.min_width, self.min_height)
        # run layout() to build basic framework of the GUI. This relies on the "gui" module
        self.layout()
        self.configure(menu=gui.menubar.MenuBar())
