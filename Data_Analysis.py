from abc import ABC, abstractmethod
from collections import defaultdict

# Define the abstract base class for analyzers
class SalesAnalyzer(ABC):
    @abstractmethod
    def analyze(self, sales_data):
        pass

# Implementing a MonthlySalesAnalyzer
class MonthlySalesAnalyzer(SalesAnalyzer):
    def analyze(self, sales_data):
        monthly_sales = defaultdict(lambda: defaultdict(int))
        for record in sales_data:
            month = record.date[:7]  # Extracting YYYY-MM from the date
            monthly_sales[record.branch][month] += record.quantity * record.price
        return monthly_sales

# Implementing a ProductPriceAnalyzer
class ProductPriceAnalyzer(SalesAnalyzer):
    def analyze(self, sales_data):
        product_prices = defaultdict(list)
        for record in sales_data:
            product_prices[record.product].append(record.price)
        return {product: sum(prices) / len(prices) for product, prices in product_prices.items()}

# Example usage
monthly_analyzer = MonthlySalesAnalyzer()
monthly_sales = monthly_analyzer.analyze(sales_data) # type: ignore
print(monthly_sales)

product_price_analyzer = ProductPriceAnalyzer()
product_prices = product_price_analyzer.analyze(sales_data) # type: ignore
print(product_prices)
