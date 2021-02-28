# Write a program that the following:

#1. Creates a list
list_1 = ["keys", "wallet", "hat", "glasses", "phone"]

#2. Alters the content to the list
list_1.append("headphones")
print(list_1)
# answer: ['keys', 'wallet', 'hat', 'glasses', 'phone', 'headphones']
#3.Extracts one item from the list and saves it as a variable
list_1.remove("hat")
print(list_1)



# answer: ['keys', 'wallet', 'hat', 'glasses', 'phone', 'headphones']
#['keys', 'wallet', 'glasses', 'phone', 'headphones']
#4.Stores the value in a dictionary with a key pointing to it.
glasses = list_1[2]
#5. Add more keys and value pairs to the dictionary
dict_1 = dict(key1 = glasses, key2 = "coffee mug", key3 = "cat food")

#6. Retrieves and prints the stored dictionary value by accessing it with a key
print(dict_1['key1'])
print(dict_1['key2'])
# answer: glasses
glasses
coffee mug
