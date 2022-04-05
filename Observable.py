from abc import ABC,abstractmethod


class Observable(ABC):
    def __init__(self,name):
        self._observers = []
        self.name=name
    @abstractmethod
    def add_observer(self,observer):
        pass
    @abstractmethod
    def delete_observer(self,observer):
        pass
    @abstractmethod
    def delete_observers(self):
        pass
    @abstractmethod
    def notify_observers(self,news):
        pass

class NewsAgency(Observable):
    def __init__(self,name):
        super().__init__(name)

    def add_observer(self,observer):
        self._observers.append(observer)
    def delete_observer(self,observer):
        self._observers.remove(observer)
    def delete_observers(self):
        self._observers=[]
    def notify_observers(self,news):
        for observer in self._observers:
            observer.update(self,news)
    def publish_news(self,news):
        self.notify_observers(news)


