# Parent Class User
class User:
    name = "Steve"
    email = "steve@gmail.com"
    password = "1234abcd"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(entry_name))
        else:
            print("The password or email is incorrect.")

#Child Class Employee
class Employee(User):
    pay_rate = "14.00"
    department = "Mens"
    pin_number = "1000"


#This is the same method in the parent class "User".
    #The difference is that, instead of using entry-password, we're using entry_pin.

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input ("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect")

#The following code invokes the methods inside each class for User and Employee.

    customer = User()
    customer.getLoginInfo()
    manager = Employee()
    manager.getLoginInfo()

#Child Class
class Sponsor:
    pay_out = "100,000"
    department = "Mens"
    pin_number = "1100"

    
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input ("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect")















if __name__ == "__main__" :
                
         

                                        
