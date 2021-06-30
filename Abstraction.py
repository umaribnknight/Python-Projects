from abc import ABC, abstractmethod

class Aircraft(ABC):

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def land(self):
        print("All checks completed")

class Jet(Aircraft):

    def fly(self):
        print("My jet is flying")

    def land(self):
        super().land()
        print("My jet has landed")
