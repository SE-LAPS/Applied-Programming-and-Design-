import unittest
from sales_data_loader import SalesDataLoader # type: ignore

class TestSalesDataLoader(unittest.TestCase):
    def test_load_data(self):
        loader = SalesDataLoader()
        data = loader.load_data('test_sales_data.csv')
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

if __name__ == '__main__':
    unittest.main()
