from abc import ABC, abstractmethod

# --- Observer Interface ---
class Observer(ABC):
    @abstractmethod
    def update(self, data):
        pass

# --- Subject ---
class Subject:
    def __init__(self):
        self._observers = []

    def register(self, observer: Observer):
        self._observers.append(observer)

    def unregister(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, data):
        for obs in self._observers:
            obs.update(data)

# --- Concrete Observers ---
class Logger(Observer):
    def update(self, data):
        print(f"[Logger] Received update: {data}")

class SpikeMonitor(Observer):
    def update(self, data):
        print(f"[SpikeMonitor] Spike event: {data}")

# --- Usage ---
subject = Subject()
subject.register(Logger())
subject.register(SpikeMonitor())

subject.notify("Neuron 12 fired")