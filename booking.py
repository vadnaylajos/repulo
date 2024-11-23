class Booking:
    def __init__(self, reservation_id, flight, passenger, booking_time, flight_date):
        self.id = reservation_id
        self.flight = flight
        self.passenger = passenger
        self.time = booking_time
        self.date = flight_date

    def total_price(self):
        return self.flight.price

    def __str__(self):
        return (
            f"Foglalási Azonosító: {self.id}, Utas: {self.passenger}, "
            f"Járat: {self.flight}, Foglalás Időpontja: {self.time}, Járat Dátuma: {self.date}"
        )