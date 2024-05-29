from abc import ABC, abstractmethod


class SalesDataObserver(ABC):
    @abstractmethod
    def update(self, data):
        pass

class SalesManager(SalesDataObserver):
    def update(self, data):
        print(f"Notification: Sales data has been updated: {data}")

class SalesDataPublisher:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, data):
        for observer in self._observers:
            observer.update(data)
