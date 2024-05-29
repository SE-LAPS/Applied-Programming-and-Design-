class DataStorage:
    def save_data(self, data):
        pass

class FileStorage(DataStorage):
    def save_data(self, data):
        # Save data to file
        pass

class SalesDataProcessor:
    def __init__(self, storage: DataStorage):
        self.storage = storage

    def process_data(self, data):
        # Process data
        self.storage.save_data(data)
