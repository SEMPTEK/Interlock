import file_manager
import session
from validate import is_empty
from tkinter import messagebox


class Project:
    name = str
    path = str
    year = int
    status = bool

    def set_status(self, state: bool):
        self.status = state

    def __init__(self, name, path):
        self.name = name
        self.path = path


# ProjectManager class used to manage the session.py project_list and all accompanying functionality
class ProjectManager:
    active_project = Project
    project_list = {}

    # add project to project list.
    def add_project(self, name, path):
        if is_empty(name):
            session.notification_manager.show_warning("Project Name Invalid. Project Not Added")
            return
        proj = Project(name, path)
        file_manager.create_local_dir(name, "Projects")
        self.append_proj_list(proj)
        self.set_active_project(name)

    # remove project from project list
    def remove_project(self, name):
        if name not in self.project_list:
            return
        # if project exists in project_list: Prompt user for confirmation of removal
        if messagebox.askyesno(title="Are You Sure?", message=f"Are you sure you would like to delete {name}?"):
            # remove project from project_list
            del self.project_list[name]
            file_manager.remove_local_dir(name, "Projects")
            file_manager.write_local("projects.dat", self.project_list)
        return

    # Append a Project object to the project list
    def append_proj_list(self, project: Project):
        # insert project into project_list. Set key for project to project name.
        self.project_list[project.name] = project
        # create data variable for appending data to project.dat file
        data = {
            str(project.name): {
                'name': str(project.name),
                'path': str(project.path),
            }
        }
        # call file_manager and append new project data, using "data" variable, to project.dat
        file_manager.append_local("projects.dat", data)
        session.navigation_frame.listbox.refresh()

    # private method for getting project list only at initialization of this class. Runs once per instance of manager.
    def __get_project_list(self, config: dict) -> dict:
        proj_list = file_manager.read_local("projects.dat")
        print(f"Discovered Projects:\n{proj_list}")
        return proj_list

    # check status of project directory in local files. Write status to each project in project_list.
    def check_path_status(self):
        for proj in self.project_list:
            self.project_list[proj].set_status(file_manager.check_path(self.project_list[proj].path))

    def set_active_project(self, proj_name):
        if proj_name in self.project_list.keys():
            self.active_project = self.project_list[proj_name]
            session.notification_manager.show(f"'{proj_name}' Set To Active Project")
            return
        session.notification_manager.show_error(f"AN ERROR OCCURRED WHILE READING {proj_name}")

    def view_project_files(self):
        file_manager.open_path_to(self.active_project.path)

    def build_list(self, config):
        proj_list = self.__get_project_list(config)
        for project in proj_list:
            name = proj_list[project]["name"]
            path = proj_list[project]["path"]
            self.project_list[project] = Project(name, path)

    # initialize class
    def __init__(self, config):
        # run private method __get_project_list (occurs once per init of this class)
        self.build_list(config)
        # check status of project paths and set as boolean in project_list[<proj>]["status"]
        self.check_path_status()
