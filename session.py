from project_manager import ProjectManager
import file_manager

name = "Companion"
config = file_manager.read_local('config.dat')
project_manager = ProjectManager(config)
