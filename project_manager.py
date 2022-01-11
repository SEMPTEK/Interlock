import file_manager
import os


class Project:
    name = str
    path = str
    year = int

    def build_path(self):
        file_manager.create_local_dir(self.name, "Projects")

    def __init__(self, name, path):
        self.name = name
        self.path = path


class ProjectManager:
    def add_project(self, name, path):
        proj = Project(name, path)
        proj.build_path()
        self.append_proj_list(proj)
        print(self.project_list)

    def append_proj_list(self, project: Project):
        self.project_list[project.name] = project
        data = {
            'name': str(project.name),
            'path': str(project.path),
        }
        file_manager.append_local("projects.dat", data)

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
