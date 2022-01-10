from modules import general, project_tracker, report_manager, rfi_manager, connector, estimator

# Add all modules to the list below and add the script files into the Module package for the software to recognize them
module_list = {
    'General': general.GeneralModule,
    'Project Tracker': project_tracker.ProjectTrackerModule,
    'Report Manager': report_manager.ReportManagerModule,
    'RFI Manager': rfi_manager.RFIManagerModule,
    'Estimator': estimator.EstimatorModule,
    'Connector': connector.Connector,
}
