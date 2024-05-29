from Data_Analysis import SalesAnalyzer


class SalesDataDecorator(SalesAnalyzer):
    def __init__(self, analyzer):
        self._analyzer = analyzer

    def analyze(self, sales_data):
        result = self._analyzer.analyze(sales_data)
        return result

class LoggingDecorator(SalesDataDecorator):
    def analyze(self, sales_data):
        print("Starting analysis")
        result = super().analyze(sales_data)
        print("Analysis complete")
        return result

# Example usage
logging_analyzer = LoggingDecorator(monthly_analyzer) # type: ignore
logging_result = logging_analyzer.analyze(sales_data) # type: ignore
print(logging_result)
