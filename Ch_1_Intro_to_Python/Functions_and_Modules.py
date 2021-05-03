# Functions

#This function takes in two different numbers as parameters and multiplies these numbers,then
# multiplies the product of those numbers by two.The functionthen returns the mutiplied
# value. The function also prints out the numerical values that have been passed in, as well as the product of manupulation.

def multiply_values(num_1, num_2):
    num_3 = 2
    print("Number 1 is : " + str(num_1))
    print("Number 2 is : " + str(num_2))
    print("Number 3 is : " + str(num_3))

    mult_num = num_1 * num_2 * num_3
    print("Product of multiplication is: " + str(mult_num))

    return mult_num

multiplied = multiply_values(8, 9)
print(multiplied)

 #Default Parameters
 # Python allows you to specify default values for variables that will be used in a function. Default values are useful because they enable the program to runwithout needing to select values for all the parameters at run mume. In order to createdefault vaules in a function, you canuse the assignment operator to assign a default value when initially creating the function.

def sample_function(variable_1, variable_2 = 9):
    #varialbe_1 = 12
    #variable_2 = 9
    print("Variable 1 is: " + str(variable_1))
    print("Variable 2 is: " + str(variable_2))

sample_function(6)

# Write a function that takes arguments and manipulates the values of those arguments in some way. Returnthe results of the manipulation. Uselocal variables in the function.

def shopping_list(store, *args):
    shopping_list = []

    for i in args:
        print("Adding {} to list".format(i))
        shopping_list.append(str(store) + " - " + str(i))

    return shopping_list
