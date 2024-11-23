from airline import Airline
from flight import DomesticFlight, InternationalFlight
from booking import Booking
from datetime import datetime
import uuid


class FlightReservationSystem:
    def __init__(self):
        # A foglalási rendszer inicializálása egy légitársasággal és mintaadatokkal
        self.reservations = []
        self.airline = Airline("SkyFly")
        self.initialize_data()

    def initialize_data(self):
        """Kezdő repülőjáratok és foglalások betöltése."""
        # Minta repülőjáratok létrehozása
        belfoldi_jarat = DomesticFlight("DF001", "Budapest", 12000)
        nemzetkozi_jarat_1 = InternationalFlight("IF101", "Dubai", 55000)
        nemzetkozi_jarat_2 = InternationalFlight("IF202", "Kathmandu", 85000)

        # Járatok hozzáadása a légitársasághoz
        self.airline.add_flight(belfoldi_jarat)
        self.airline.add_flight(nemzetkozi_jarat_1)
        self.airline.add_flight(nemzetkozi_jarat_2)

        # Mintafoglalások létrehozása egyedi azonosítóval
        self.reservations.append(Booking(self.generate_id(), belfoldi_jarat, "Tihamer", datetime.now(), "2024-12-01"))
        self.reservations.append(Booking(self.generate_id(), nemzetkozi_jarat_1, "Gipsz Jakab", datetime.now(), "2024-12-05"))
        self.reservations.append(Booking(self.generate_id(), nemzetkozi_jarat_2, "Gipsz Jakabne", datetime.now(), "2024-12-10"))
        self.reservations.append(Booking(self.generate_id(), nemzetkozi_jarat_2, "if. Gipsz Jaki", datetime.now(), "2024-12-10"))

    def generate_id(self):
        """Egyedi azonosító generálása minden foglaláshoz."""
        return str(uuid.uuid4())

    def create_reservation(self, flight_number, passenger_name, flight_date):
        """
        Új foglalás létrehozása, ha a járat létezik és a dátum érvényes.

        Args:
            flight_number (str): A foglalni kívánt járatszám.
            passenger_name (str): Az utas neve.
            flight_date (str): A járat dátuma ÉÉÉÉ-HH-NN formátumban.
        """
        flight = self.find_flight(flight_number)
        if flight:
            try:
                booking_date = datetime.now()
                flight_date_parsed = datetime.strptime(flight_date, "%Y-%m-%d")
                if flight_date_parsed <= booking_date:
                    print("Hiba: A járat dátuma csak a jövőben lehet, hacsak nincs időgéped!")
                    return
                # Új foglalás létrehozása egy egyedi ID-val
                unique_id = self.generate_id()
                new_reservation = Booking(unique_id, flight, passenger_name, booking_date, flight_date)
                self.reservations.append(new_reservation)
                print("Foglalás sikeres! 🎉")
                print(f"Foglalási azonosító: {unique_id}")
                print(f"Költség: {new_reservation.total_price()} Ft, Járat dátuma: {flight_date}")
            except ValueError:
                print("Érvénytelen dátumformátum. Használja az ÉÉÉÉ-HH-NN formátumot (pl.: 2024-12-15).")
        else:
            print("Nem található járat ezzel a számmal. Kérlek, nézd meg újra!")

    def cancel_reservation(self, reservation_id):
        """
        Foglalás törlése az egyedi foglalási azonosító alapján.

        Args:
            reservation_id (str): A törölni kívánt foglalás egyedi azonosítója.
        """
        for reservation in self.reservations:
            if reservation.id == reservation_id:
                self.reservations.remove(reservation)
                print("Foglalás sikeresen törölve. Azt mondják, törölni emberi dolog!")
                return
        print("Nem található foglalás ezzel az azonosítóval. Lehet, hogy csak álmodtad?")

    def show_reservations(self):
        """Az összes aktív foglalás megjelenítése."""
        if not self.reservations:
            print("Nincsenek aktív foglalások. Üresek az ülések, mint a sivatag!")
        else:
            for reservation in self.reservations:
                print(reservation)

    def find_flight(self, flight_number):
        """Keres és visszaad egy járatot a járatszám alapján."""
        return next((flight for flight in self.airline.flights if flight.number == flight_number), None)


if __name__ == "__main__":
    system = FlightReservationSystem()
    while True:
        # A főmenü megjelenítése
        print("\n--- Repülőjegy Foglalási Rendszer ---")
        print("A. Új Foglalás Létrehozása")
        print("B. Foglalás Törlése")
        print("C. Foglalások Megtekintése")
        print("D. Elérhető Járatok Megtekintése")
        print("E. Kilépés")
        choice = input("Válassz egy opciót: ").upper()

        if choice == "A":
            # Új foglalás létrehozása
            system.airline.display_flights()
            flight_num = input("Járatszám: ")
            name = input("Utas neve: ")
            date = input("Járat dátuma (ÉÉÉÉ-HH-NN): ")
            system.create_reservation(flight_num, name, date)
        elif choice == "B":
            # Foglalás törlése
            reservation_id = input("Add meg a törölni kívánt foglalás azonosítóját: ")
            system.cancel_reservation(reservation_id)
        elif choice == "C":
            # Aktív foglalások megtekintése
            system.show_reservations()
        elif choice == "D":
            # Elérhető járatok megtekintése
            system.airline.display_flights()
        elif choice == "E":
            print("Kilépés a programból. Köszönjük, hogy velünk repültél! Reméljük, újra találkozunk az égben! ✈️")
            break
        else:
            print("Érvénytelen opció. Próbáld újra, mert ez most nem volt sikeres.")