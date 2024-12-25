from dal.Repository import Repository
from  be.server import M_Hazine
from datetime import datetime
from collections import defaultdict
class addplan():
    def __init__(self):
        self.repository = Repository()

    def GetDataHistory(self):
        repso = Repository()
        return repso.Read(M_Hazine)

    def GetTotalHazine(self):
        total_hazine = 0
        for hazine in self.GetDataHistory():
            total_hazine += hazine.hazine  # Assuming 'hazine' is the field for the amount
        return total_hazine

    def GetMonthlyHazine(self):
        hazine_data = defaultdict(int)
        today = datetime.today()
        current_month = today.month
        current_year = today.year

        for hazine in self.GetDataHistory():
            hazine_date = hazine.time
            if hazine_date.year == current_year and hazine_date.month == current_month:
                hazine_data[hazine_date.day] += hazine.hazine

        monthly_hazine = [hazine_data[day] for day in range(1, 32)]
        return monthly_hazine
    