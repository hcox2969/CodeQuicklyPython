# For Loops and Errors EXERCISE

# Create a list or seauence

# Use a for loop to iterate through the list and do something with the items in the list

# Break the for loop under some condition

# Include some type of error handling


num_list = [92, 11, 33, 59, 12, 65, 9, 43, 55, 1]

search_term = input("Enter a number to divide by: ")

print("Starting loop")

for num in num_list:
    try:
        num = num//int(search_term)
        print(num)
    except:
        print("Incompatiable divisor entered.")
        break

print("Loop ended")
