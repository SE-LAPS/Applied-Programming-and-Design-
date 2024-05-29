from ISP import SalesDataLoader


def test_integration():
    loader = SalesDataLoader()
    data = loader.load_data('test_sales_data.csv')
    analyzer = MonthlySalesAnalyzer() # type: ignore
    result = analyzer.analyze(data)
    assert isinstance(result, dict)
    assert len(result) > 0
