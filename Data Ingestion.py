from collections import namedtuple
import csv

SalesRecord = namedtuple('SalesRecord', ['branch', 'product', 'date', 'quantity', 'price'])

class SalesDataLoader:
    def load_data(self, file_path):
        sales_data = []
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                record = SalesRecord(branch=row['Branch'], product=row['Product'], date=row['Date'],
                                     quantity=int(row['Quantity']), price=float(row['Price']))
                sales_data.append(record)
        return sales_data
