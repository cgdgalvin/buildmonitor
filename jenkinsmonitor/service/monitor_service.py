

class MonitorService:

    targeryen_jobs = ['VI Data Warehouse - Unit Test', 'Create Staging Tables', 'Run Stored Procedures',
                 'VI Data Warehouse - Integration Test', 'VI Data Warehouse Test',
                 'Transformation Runner - DAL TC (UAT)', 'Transformation Runner - DAL (LIVE)',
                 'Transformation Runner - DAL TC (LIVE)']

    def get_jobs_list(self, monitor):
        if monitor == 1:
            return self.targeryen_jobs
        return []