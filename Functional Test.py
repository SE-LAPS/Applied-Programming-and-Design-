from Data_Analysis import MonthlySalesAnalyzer
from ISP import SalesDataLoader
from Report_Generation import ReportGenerator


def test_generate_report():
    loader = SalesDataLoader()
    data = loader.load_data('test_sales_data.csv')
    analyzer = MonthlySalesAnalyzer()
    analysis_result = analyzer.analyze(data)
    report_generator = ReportGenerator()
    report = report_generator.generate_report(analysis_result, 'monthly_sales')
    assert 'Branch' in report
    assert 'Month' in report
