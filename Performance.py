from ISP import SalesDataLoader
from locust import HttpUser, task # type: ignore

class SalesDataProcessingUser(HttpUser):
    @task
    def load_and_analyze_data(self):
        loader = SalesDataLoader()
        data = loader.load_data('large_sales_data.csv')
        analyzer = MonthlySalesAnalyzer() # type: ignore
        analyzer.analyze(data)
