from abc import ABC, abstractmethod

class Flight(ABC):
    def __init__(self, number, destination, price):
        self.number = number
        self.destination = destination
        self.price = price

    @abstractmethod
    def details(self):
        pass

class DomesticFlight(Flight):
    def details(self):
        return f"Domestic Flight - Number: {self.number}, Destination: {self.destination}, Price: {self.price} Ft"

class InternationalFlight(Flight):
    def details(self):
        return f"International Flight - Number: {self.number}, Destination: {self.destination}, Price: {self.price} Ft"
