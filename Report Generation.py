class ReportGenerator:
    def generate_report(self, analysis_result, report_type):
        if report_type == 'monthly_sales':
            for branch, sales in analysis_result.items():
                print(f'Branch: {branch}')
                for month, total in sales.items():
                    print(f'  Month: {month}, Total Sales: {total}')
        elif report_type == 'product_prices':
            for product, avg_price in analysis_result.items():
                print(f'Product: {product}, Average Price: {avg_price}')
