import datetime

# This are personal notes intended to exemplify Object-Oriented Programming use cases

# A class encapsulates data and functionality - data as attributes, and functionality as methods. 
# It is a blueprint to create concrete instances in the memory.


class Employee:
    """Blueprint of an Employee (parent class)"""
    # Class attributes
    num_of_emp = 0 # assign initial number of employees
    raise_amount = 1.07 # assign a % salary increase (e.g. 7%)
    

    # define the initialise method (also known as constructor)
    def __init__(self, firstname, lastname, salary):
        """The properties that all Employee objects must have are defined in a method called .__init__(). 
        Every time a new Employee object is created, .__init__() sets the initial state of the object 
        by assigning the values of the object’s properties. 
        That is, .__init__() initializes each new instance of the class.
        Attributes created in .__init__() are called instance attributes."""
        # create Employee class instances
        self.firstname = firstname 
        self.lastname = lastname
        self.salary = salary # can be non-public (encapsulated "self._salary" or more private "self.__salary" )

        # add new employees to num_of_emp
        Employee.num_of_emp += 1
    

    # salary increase instance method
    def apply_raise(self):
        """This function return the new salary applying the specified raise"""
        self.salary = int(self.salary * self.raise_amount) # calculate the new salary 
        #self.salary = int(self.salary * Employee.raise_amount) # calc the new salary


    # Creating Property Decorators ---> Getters, Setters, Deleters
    @property
    def email(self):
        """This function will generate an email based on given condition"""
        return f"{self.firstname}.{self.lastname}@email.com"

    @property
    def fullname(self):
        """This function will generate the fullname based on given condition"""
        return f"{self.firstname} {self.lastname}"

    @fullname.setter
    def fullname(self, name):
        firstname, lastname = name.split(' ')
        self.firstname = firstname
        self.lastname = lastname

    @fullname.deleter
    def fullname(self):
        print("Delete name.")
        self.firstname = None
        self.lastname = None

    

    # Alternative constructors
    # A class method is a method that is bound to the class and not the object of the class.
    # They have the access to the state of the class as it takes a class parameter that points to the class 
    # and not the object instance. It can modify a class state that would apply across all the instances of the class. 
    # For example, it can modify a class variable that will be applicable to all the instances.
    # We generally use the class method to create factory methods. 
    # Factory methods return class objects ( similar to a constructor ) for different use cases
    @classmethod 
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount 

    @classmethod
    def from_string(cls, emp_str):
        firstname, lastname, salary = emp_str.split(",")
        return cls(firstname, lastname, salary)
    

    # A static method does not receive an implicit first argument. 
    # A static method is also a method that is bound to the class and not the object of the class. 
    # This method can’t access or modify the class state.
    # We generally use static methods to create utility functions
    @staticmethod
    def is_workday(day):
        """Returns if it is a workday or not"""
        if day.weekday() == 5 or day.weekday == 6: # Saturday or Sunday
            return False
        return True

### Creating special methods (Dunder)
    def __repr__(self):
        return f"Employee ({self.firstname} {self.lastname}, {self.salary})"


# Inheritance is the process by which one class takes on the attributes and methods of another. 
# Newly formed classes are called child classes, 
# and the classes that child classes are derived from are called parent classes.
# Child classes can override or extend the attributes and methods of parent classes. 
# In other words, child classes inherit all of the parent’s attributes and methods 
# but can also specify attributes and methods that are unique to themselves.
class Developer(Employee):
    """This is a subclass of the parent class Employee"""
    #raise_amount = 1.03

    def __init__(self, firstname, lastname, salary, prog_language):
        super().__init__(firstname, lastname, salary) # inherited from Employee class
        self.prog_language = prog_language # unique attribute
    

dev_1 = Developer("John", "Doe", 60000, "Python")
dev_2 = Developer("Ann", "Smith", 70000, "Java")

class Manager(Employee):
    """This is a subclass of the parent class Employee"""
    def __init__(self, firstname, lastname, salary, employees=None):
        super().__init__(firstname, lastname, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        """Add a new employee"""
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        """Remove an employee"""
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        """Return the fullname of employees"""
        for emp in self.employees:
            print("--->", emp.fullname())

mgr_1 = Manager("Joe", "Williams", 100000, [dev_1])


####################### Code Practice ###############################

###   Checking for a workday date
#my_date = datetime.date(2023, 1, 25)
#print(Employee.is_workday(my_date))


###   Adding a new employee and set email and pay raise
#emp_str_1 = "Mary,Ross,86000"
#new_emp_1 = Employee.from_string(emp_str_1)
#print(new_emp_1.email)
#Employee.set_raise_amount(1.02)


###   Adding employees details
#emp_1 = Employee("John", "Doe", 60000)
#emp_2 = Employee("Ann", "Smith", 70000)


#print(repr(emp_1))
#print(str(emp_2))
#print(emp_1.__str__())


###   Displaying email and fullname
#print(emp_1.email)
#print(emp_2.fullname())
#print(Employee.fullname(emp_1))


###   Adding pay raise for Employee class / a single employee
#print(Employee.raise_amount)
#print(emp_2.raise_amount)


###   Check for an employee salary before and after pay raise
#print(emp_2.salary)
#emp_2.apply_raise()
#print(emp_2.salary)


###   Displays Employee class / a single employee details into a dictionary
#print(emp_1.__dict__) # displays a dict of emp_1
#print(Employee.__dict__)


###   Adding pay raise for a single employee (displaying also the pay raise)
#emp_1.raise_amount = 1.09
#print(emp_1.salary)
#print(emp_1.__dict__)


###   Displaying the total number of employees
#print(Employee.num_of_emp)


### Displaying dev_1 email and prog_language 
#print(dev_1.email)
#print(dev_1.prog_language)


### Displaying dev_1 salary before and after the specified raise
#print(dev_1.salary)
#dev_1.apply_raise()
#print(dev_1.salary)


### Return whether an object (mgr_1) is part of a particular class
#print(isinstance(mgr_1, Manager)) 


### Return whether 'cls' is derived from another class or is the same class
#print(issubclass(Manager, Developer)) 




