from abc import ABC,abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self,observable,news):
        pass

class Newspaper(Observer):
    def __init__(self,name):
        self.name=name
    def update(self, observable,news):
        print("{0} ({1}) : {2}".format(self.name,observable.name, news))

class SMS(Observer):
    def __init__(self,phone_number):
        self.phone_number=phone_number
    def update(self,observable,news):
        print("{0} ({1}) : {2}".format(self.phone_number, observable.name, news))