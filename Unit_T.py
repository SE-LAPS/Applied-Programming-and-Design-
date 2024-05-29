import unittest
from sales_data_loader import SalesDataLoader # type: ignore
from sales_analyzer import MonthlySalesAnalyzer # type: ignore

class TestSalesDataLoader(unittest.TestCase):
    def test_load_data(self):
        loader = SalesDataLoader()
        data = loader.load_data('test_sales_data.csv')
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

class TestMonthlySalesAnalyzer(unittest.TestCase):
    def test_analyze(self):
        loader = SalesDataLoader()
        data = loader.load_data('test_sales_data.csv')
        analyzer = MonthlySalesAnalyzer()
        result = analyzer.analyze(data)
        self.assertIsInstance(result, dict)
        self.assertGreater(len(result), 0)

if __name__ == '__main__':
    unittest.main()
