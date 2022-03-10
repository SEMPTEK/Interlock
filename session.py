from project_manager import ProjectManager
import file_manager

name = "Interlock"
config = file_manager.read_local('config.dat')
project_manager = ProjectManager(config)
notification_manager = None
navigation_frame = None
tab_manager = None
winfo = {
    'width': "1920",
    'height': "2080",
}
