from ISP import SalesDataLoader
from Notification import SalesDataPublisher, SalesManager


def main():
    loader = SalesDataLoader()
    sales_data = loader.load_data('sales_data.csv')
    
    monthly_analyzer = MonthlySalesAnalyzer() # type: ignore
    product_price_analyzer = ProductPriceAnalyzer() # type: ignore
    
    monthly_sales = monthly_analyzer.analyze(sales_data)
    product_prices = product_price_analyzer.analyze(sales_data)
    
    report_generator = report_generator()
    report_generator.generate_report(monthly_sales, 'monthly_sales')
    report_generator.generate_report(product_prices, 'product_prices')
    
    publisher = SalesDataPublisher()
    manager = SalesManager()
    publisher.register_observer(manager)
    publisher.notify_observers("New analysis has been completed")

if __name__ == "__main__":
    main()
