import file_manager
import os


class Project:
    name = str
    path = str
    year = int

    def build_path(self):
        file_manager.create_local_dir(self.name)

    def __init__(self, name, path):
        self.name = name
        self.year = path


class ProjectManager:
    def add_project(self, name, path):
        proj = Project(name, path)
        self.project_list[name] = proj

    def __get_project_list(self, config: dict) -> dict:
        proj_list = file_manager.read_local("projects.dat")
        print(f"Discovered Projects:\n{proj_list}")
        return proj_list

    def check_path_status(self):
        for proj in self.project_list:
            self.project_list[proj]["status"] = file_manager.check_path(self.project_list[proj]["path"])

    def __init__(self, config):
        self.project_list = self.__get_project_list(config)
        self.check_path_status()
