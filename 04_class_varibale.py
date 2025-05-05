"""4. Class Variables and Class Methods
Assignment:
Create a class Bank with a class variable bank_name. Add a class
 method change_bank_name(cls, name) 
 that allows changing the bank name. Show that it affects all instances."""

class Bank:
    bank_name = "old bank"

    def __init__(self, account_holder):
        self.account_number = account_holder
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
    
    def show_details(self):
        print(f"Account Holder: {self.account_number}")
        print(f"Bank Name: {self.bank_name}")


acc1 = Bank("Alice")
acc2 = Bank("Bob")


acc1.show_details()  # Account Holder: Alice, Bank Name: old bank
acc2.show_details()  # Account Holder: Bob, Bank Name: old bank
Bank.change_bank_name("new bank")

print("After changing bank name:")
acc1.show_details()  # Account Holder: Alice, Bank Name: new bank
acc2.show_details()  # Account Holder: Bob, Bank Name: new bank
