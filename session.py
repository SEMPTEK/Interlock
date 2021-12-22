from project_manager import ProjectManager
from file_manager import read_local

name = "Companion"
config = read_local('config.dat')
project_manager = ProjectManager(config)
gui_data = {
    'frames': {}
}
