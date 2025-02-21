class Customer:
    def __init__(self, name, room_number, balance):
        self.name = name
        self.room_number = room_number
        self.__balance = balance  # Private variable
    
    def get_balance(self):
        return self.__balance
    
    def update_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance update!")

    def display_info(self):
        return f"Name: {self.name}, Room: {self.room_number}, Balance: {self.__balance:.2f}"
