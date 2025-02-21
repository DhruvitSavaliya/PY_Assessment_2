from database import Database
from customer import Customer

class Hotel:
    def __init__(self):
        self.db = Database()
    
    def check_in(self, name, room_number, balance):
        guest = Customer(name, room_number, balance)
        self.db.execute_query("INSERT INTO guests (name, room_number, balance) VALUES (%s, %s, %s)", 
                              (guest.name, guest.room_number, guest.get_balance()))
        print("Guest ",guest.name," checked in successfully!")

    def check_out(self, room_number):
        self.db.execute_query("DELETE FROM guests WHERE room_number = %s", (room_number,))
        print("Room ",room_number," checked out successfully!")

    def display_guests(self):
        guests = self.db.fetch_data("SELECT * FROM guests")
        for guest in guests:
            print(f"ID: {guest[0]}, Name: {guest[1]}, Room: {guest[2]}, Balance: {guest[4]:.2f}")
