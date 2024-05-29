from ISP import SalesDataLoader


def test_generate_report():
    loader = SalesDataLoader()
    data = loader.load_data('test_sales_data.csv')
    analyzer = MonthlySalesAnalyzer() # type: ignore
    analysis_result = analyzer.analyze(data)
    report_generator = ReportGenerator() # type: ignore
    report = report_generator.generate_report(analysis_result, 'monthly_sales')
    assert 'Branch' in report
    assert 'Month' in report
