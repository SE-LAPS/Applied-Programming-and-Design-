class SalesDataDecorator(SalesAnalyzer): # type: ignore
    def __init__(self, analyzer):
        self._analyzer = analyzer

    def analyze(self, sales_data):
        result = self._analyzer.analyze(sales_data)
        # Add additional behavior
        return result

class LoggingDecorator(SalesDataDecorator):
    def analyze(self, sales_data):
        print("Starting analysis")
        result = super().analyze(sales_data)
        print("Analysis complete")
        return result
