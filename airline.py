class Airline:
    def __init__(self, name):
        self.name = name
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def display_flights(self):
        if not self.flights:
            print("Nincsenek elérhető járatok. Úgy tűnik, most egy csendes nap van!")
        else:
            print(f"\nElérhető Járatok ({self.name}):")
            for flight in self.flights:
                print(f"Járatszám: {flight.number}")

    def __str__(self):
        return f"Légitársaság: {self.name}, Összes Járat: {len(self.flights)}"