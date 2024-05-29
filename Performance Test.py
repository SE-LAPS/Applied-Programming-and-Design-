from Data_Analysis import MonthlySalesAnalyzer
from ISP import SalesDataLoader
from locust import HttpUser, task # type: ignore

class SalesDataProcessingUser(HttpUser):
    @task
    def load_and_analyze_data(self):
        loader = SalesDataLoader()
        data = loader.load_data('large_sales_data.csv')
        analyzer = MonthlySalesAnalyzer()
        analyzer.analyze(data)
