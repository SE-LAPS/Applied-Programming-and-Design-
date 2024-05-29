from Data_Analysis import MonthlySalesAnalyzer, ProductPriceAnalyzer


class AnalyzerFactory:
    def create_analyzer(self, analyzer_type):
        if analyzer_type == 'monthly':
            return MonthlySalesAnalyzer()
        elif analyzer_type == 'price':
            return ProductPriceAnalyzer()
        # Add more analyzers as needed

# Example usage
factory = AnalyzerFactory()
monthly_analyzer = factory.create_analyzer('monthly')
monthly_sales = monthly_analyzer.analyze(sales_data) # type: ignore
print(monthly_sales)
