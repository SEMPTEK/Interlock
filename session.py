from project_manager import ProjectManager
import configuration
import file_manager

name = "Interlock"
config = configuration.load()
project_manager = ProjectManager(config)
notification_manager = None
navigation_frame = None
tab_manager = None
winfo = {
    'width': "1920",
    'height': "2080",
}
