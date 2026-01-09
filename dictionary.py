# Sample dictionary
my_dict = {
'a': 10,
'b': 20,
'c': 30,
'd': 40,
'e': 50
}
​
# Initialize a variable to store the sum
total_sum = 0
​
# Iterate through the values of the dictionary and add them to the tota
for i in my_dict.values():
total_sum += i
​
# Print the sum of all items in the dictionary
print("Sum of all items in the dictionary:", total_sum)
######################################################################


# 1. Using the update() method:
​
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
​
dict1.update(dict2)
​
# The merged dictionary is now in dict1
print("Merged Dictionary (using update()):", dict1)

####################################################################

# 2. Using dictionary unpacking
​
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
​
# Merge dict2 into dict1 using dictionary unpacking
merged_dict = {**dict1, **dict2}
​
# The merged dictionary is now in merged_dict
print("Merged Dictionary (using dictionary unpacking):", merged_dict)



