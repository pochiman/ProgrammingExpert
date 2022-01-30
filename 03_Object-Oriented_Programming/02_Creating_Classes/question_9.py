##### ContactInformation Class #####
# Create a ContactInformation class that is instantiated by passing a first_name, last_name, 
# email and phone_number.  This class should store all of the passed values as instance 
# attributes and have an additional attribute country that is set by default to None.

# After creating the class, instantiate two instances of it.  The first instance should be 
# stored in the variable person1 and the next in person2.

class ContactInformation:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.country = None


person1 = ContactInformation(
    "Joe", "Smith", "JoeSmith@algoexpert.io", "905-999-9999")
person2 = ContactInformation(
    "Sarah", "Jones", "SarahJones@algoexpert.io", "416-333-2134")