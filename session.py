from file_manager import FileManager

name = "Companion"
file_manager = FileManager()
config_data = file_manager.read_local("config.dat")
