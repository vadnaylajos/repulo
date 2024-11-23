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
            f"Reservation ID: {self.id}, Passenger: {self.passenger}, "
            f"Flight: {self.flight.details()}, Booking Time: {self.time}, Flight Date: {self.date}"
        )
