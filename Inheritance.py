#Create two classes that inherit from another class.
#Ensure each child has at least two of their own attributes.






class User:
#Define the attribute of parent class
   name = 'No Name Provided'
   email = ' '
   password = '1234abcd'
   account_number = 0

class Driver(User):
#child class
    base_pay = 20.00
    department = 'Delivery'

class Customer(User):
#child class
    delivery_address = ' '
    delivery_list = True
