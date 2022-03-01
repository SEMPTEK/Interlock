from modules import general, project_tracker, report_manager, rfi_manager, add_project, estimator, remove_project
from modules import edit_project

# Add all modules to the list below and add the script files into the Module package for the software to recognize them
module_list = {
    # Name: (<Object>, <visible on startup T/F>)
    'General': (general.GeneralModule, True),
    'Project Tracker': (project_tracker.ProjectTrackerModule, True),
    'Report Manager': (report_manager.ReportManagerModule, True),
    'RFI Manager': (rfi_manager.RFIManagerModule, True),
    'Estimator': (estimator.EstimatorModule, True),
    'Add Project': (add_project.AddProjectFrame, False),
    'Remove Projects': (remove_project.RemoveProjectModule, False),
    'Edit Project': (edit_project.ProjectEditModule, False),
}
