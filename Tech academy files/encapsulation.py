# program to illustrate protected access modifier in a class
  
# super class
class troops:
     
     # protected data members
     _name = None
     _unit = None
     _branch = None
     
     # constructor
     def __init__(self, name, roll, branch):  
          self._name = name
          self._unit = unit
          self._branch = branch
     
     # protected member function   
     def _displayUnitAndBranch(self):
  
          # accessing protected data members
          print("Unit: ", self._unit)
          print("Branch: ", self._branch)
  
  
# derived class
class Marine(Troops):
  
       # constructor 
       def __init__(self, name, unit, branch): 
                Student.__init__(self, name, unit, branch) 
          
       # public member function 
       def displayDetails(self):
                    
                 # accessing protected data members of super class 
                print("Name: ", self._name) 
                    
                 # accessing protected member functions of super class 
                self._displayUnitAndBranch()
  
# creating objects of the derived class        
obj = Troops("R2J", 1706256, "Information Technology") 
  
# calling public member functions of the class
obj.displayDetails()


# program to illustrate private access modifier in a class
  
class Infantry:
     
     # private members
     __name = None
     __unit = None
     __branch = None
  
     # constructor
     def __init__(self, name, unit, branch):  
          self.__name = name
          self.__unit = unit
          self.__branch = branch
  
     # private member function  
     def __displayDetails(self):
            
           # accessing private data members
           print("Name: ", self.__name)
           print("Unit: ", self.__unit)
           print("Branch: ", self.__branch)
     
     # public member function
     def accessPrivateFunction(self): 
             
           # accesing private member function
           self.__displayDetails()  
  
# creating object    
obj = Infantry("R2J", 1706256, "Information Technology")
  
# calling public member function of the class
obj.accessPrivateFunction()
