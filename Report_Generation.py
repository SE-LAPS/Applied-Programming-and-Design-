class ReportGenerator:
    def generate_report(self, analysis_result, report_type):
        if report_type == 'monthly_sales':
            report = ""
            for branch, sales in analysis_result.items():
                report += f'Branch: {branch}\n'
                for month, total in sales.items():
                    report += f'  Month: {month}, Total Sales: {total}\n'
            return report
        elif report_type == 'product_prices':
            report = ""
            for product, avg_price in analysis_result.items():
                report += f'Product: {product}, Average Price: {avg_price}\n'
            return report

# Example usage
report_generator = ReportGenerator()
monthly_sales_report = report_generator.generate_report(monthly_sales, 'monthly_sales') # type: ignore
print(monthly_sales_report)

product_prices_report = report_generator.generate_report(product_prices, 'product_prices') # type: ignore
print(product_prices_report)
