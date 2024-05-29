from abc import ABC, abstractmethod
from unittest import loader


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class LoadDataCommand(Command):
    def __init__(self, loader, file_path):
        self.loader = loader
        self.file_path = file_path

    def execute(self):
        return self.loader.load_data(self.file_path)

class AnalyzeDataCommand(Command):
    def __init__(self, analyzer, data):
        self.analyzer = analyzer
        self.data = data

    def execute(self):
        return self.analyzer.analyze(self.data)

# Example usage
load_command = LoadDataCommand(loader, 'sales_data.csv')
data = load_command.execute()

analyze_command = AnalyzeDataCommand(monthly_analyzer, data) # type: ignore
result = analyze_command.execute()
print(result)
