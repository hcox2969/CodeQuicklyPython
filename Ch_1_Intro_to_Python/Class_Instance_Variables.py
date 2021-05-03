# 05/03/21
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
