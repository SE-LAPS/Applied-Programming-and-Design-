class AnalyzerFactory:
    def create_analyzer(self, analyzer_type):
        if analyzer_type == 'monthly':
            return MonthlySalesAnalyzer() # type: ignore
        elif analyzer_type == 'price':
            return ProductPriceAnalyzer() # type: ignore
        # Add more analyzers as needed
