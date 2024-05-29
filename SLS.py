class SalesDataObserver:
    def update(self, data):
        raise NotImplementedError

class SalesManager(SalesDataObserver):
    def update(self, data):
        print(f"Sales data updated: {data}")

class SalesDataPublisher:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, data):
        for observer in self._observers:
            observer.update(data)

# Usage
publisher = SalesDataPublisher()
manager = SalesManager()
publisher.register_observer(manager)
publisher.notify_observers("New sales data available")
