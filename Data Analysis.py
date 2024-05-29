from abc import Data_Labs, abstractmethod
from collections import defaultdict

class SalesAnalyzer(Data_Labs):
    @abstractmethod
    def analyze(self, sales_data):
        pass

class MonthlySalesAnalyzer(SalesAnalyzer):
    def analyze(self, sales_data):
        monthly_sales = defaultdict(lambda: defaultdict(int))
        for record in sales_data:
            month = record.date[:7]  # Extracting YYYY-MM from the date
            monthly_sales[record.branch][month] += record.quantity * record.price
        return monthly_sales

class ProductPriceAnalyzer(SalesAnalyzer):
    def analyze(self, sales_data):
        product_prices = defaultdict(list)
        for record in sales_data:
            product_prices[record.product].append(record.price)
        return {product: sum(prices)/len(prices) for product, prices in product_prices.items()}
