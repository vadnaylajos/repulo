class Airline:
    def __init__(self, name):
        self.name = name
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def display_flights(self):
        if not self.flights:
            print("No flights available.")
        else:
            print(f"\nAvailable Flights ({self.name}):")
            for flight in self.flights:
                print(flight.number)

    def __str__(self):
        return f"Airline: {self.name}, Total Flights: {len(self.flights)}"
