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
    project_list = {}

    def add_project(self, name, year):
        proj = Project(name, year)
        self.project_list[year][name] = proj

    def add_year(self, year):
        self.project_list[year] = {}

    def __get_project_list(self, config: dict) -> list:
        proj_list = file_manager.list_local("Projects")
        return proj_list

    def __init__(self, config):
        self.project_list = self.__get_project_list(config)
