import file_manager
import os


class Project:
    name = str
    path = str
    year = int

    def build_path(self):
        file_manager.create_local_dir(self.name, self.path)

    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.path = os.path.join(self.year, self.name)


class ProjectManager:
    def add_project(self, name, year):
        proj = Project(name, year)
        self.project_list[year][name] = proj

    def add_year(self, year):
        self.project_list[year] = {}

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
