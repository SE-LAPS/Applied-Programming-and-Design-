class SalesReport:
    def generate(self):
        pass

class BranchSalesReport(SalesReport):
    def generate(self):
        # Specific branch sales report generation
        pass

def generate_report(report: SalesReport):
    report.generate()

generate_report(BranchSalesReport())
