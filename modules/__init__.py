from modules import general, project_tracker, report_manager, rfi_manager, add_project, estimator

# Add all modules to the list below and add the script files into the Module package for the software to recognize them
module_list = {
    # Name: (<Object>, <visible on startup T/F>)
    'General': (general.GeneralModule, True),
    'Project Tracker': (project_tracker.ProjectTrackerModule, False),
    'Report Manager': (report_manager.ReportManagerModule, False),
    'RFI Manager': (rfi_manager.RFIManagerModule, False),
    'Estimator': (estimator.EstimatorModule, False),
    'Add Project': (add_project.Connector, False),
}
