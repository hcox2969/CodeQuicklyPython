# 05/03/21
#INSCTANCE METHOD
#Methods are basically funcitons that belong to a class. They are used to carry out specific tasks but they can only be used directly on an object that has been created using the class blueprint.

# initialiing class as a blueprint for other objects. Class employee represents
# employees, tracks their attributes, like user_name, email and role
# and allows to update their attributes.

class Employee:
    # place the variable outside a method under the main scole of class:
    location = "Seattle, WA"
# location variable is created outsid ethe instance constructor, and this means
# that the variable applies to all instances of the class that are created.
# As a class variable, it applies to all instances, reflecting that all
# employees are in one physical location.

    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role

# add a method to the class we created above that can be used to print out
# the name, email and role of an instance, all with one method.

    def get_info(self):
        return '{}, {}, {}'.format(self.name, self.email, self.role)

# Using a class method, we can change the location class variable we created above. We will create a class method that operats on the class. We will use the @classmethod decorator and pass in cls as the first argument. We then update the class location to a new location we pass in when we call the method. We will create a new employee to test th enew class method.
    @classmethod
    def change_locale(cls, new_location):
        cls.location = new_location

employee_3 = Employee("R. Acevedo", "Racevedo@business.com", "Developer")

print(employee_3.location)
Employee.change_locale('Los Angeles, CA')
print(employee_3.location)


# creating an actual object using the class blueprint. We pass the arguments
# consisting of values we want the class to use, in the order they appear above.
# this is called an instance of a class:
employee_1 = Employee("E. Davis", "edavis@business.com", "Hiring Manager")
employee_2 = Employee("D. Wong", "dwong@business.com", "Developer")

# After the instances of a class have been created, we can access the individual
# elements of the class and update them. We access the desired attributes
# using dot notation and update the value of an attribute siply by assigning
# it a new value.
print (employee_1.role)
print (employee_1.email)
# now update the role for employee_1:
employee_1.role = "Lead Developer"
print(employee_1.role)

print(employee_1.location)
print(employee_2.location)

print (employee_1.get_info())
# an alternative way of calling our method, calling it directly on the class,
# and then passing in the desired instance.
print (Employee.get_info(employee_1))
# CLASS  method
# Decorator
# The decorator starts with @ symbol and is placed directly above the line
# containing the def keyword that starts the method.
# STATIC METHOD
# Static methods are the methos that receive neither an instance nor a class when they are called. Static methods are bound to a class instea of an object, and they deal with parameters of the class. Since static methods can't access the properties of the class itself, they have limited use cases. Static methods are typically only used when a utility function is required that doesn't operate on any proerpteis of a class, but makes sence for the method to belong to the class. 
