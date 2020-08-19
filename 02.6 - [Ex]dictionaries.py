# SOURCE: https://www.w3schools.com/python/python_dictionaries.asp

# A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.
print('--Example 1--')
# Create and print a dictionary:
sw2 = {
    'device_type': 'cisco_ios',
    'host': '192.168.122.92',
    'username': 'admin',
    'password': 'cisco',
}
print(sw2)

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:
print('\n--Example 2--')
x = sw2['device_type']
print('Device Type = ' + x)
# There is also a method called get() that will give you the same result:
x = sw2.get('host')
print('IP address = ' + x)

# Change Values
# You can change the value of a specific item by referring to its key name:
print('\n--Example 3--')
x = sw2['username']
print('Username = ' + x)
sw2['username'] = 'cisco'
x = sw2['username']
print('Username = ' + x)

print('\n--Example 4--')
# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary,
# but there are methods to return the values as well.
print('#Print all key names in the dictionary, one by one:')
for i in sw2:
    print(i)

print('#Print all values in the dictionary, one by one:')
for i in sw2:
    print(sw2[i])

print('#You can also use the values() method to return values of a dictionary:')
for i in sw2.values():
    print(i)

print('#Loop through both keys and values, by using the items() method:')
for i, n in sw2.items():
    print(i + ' -> ' + n)

print('\n--Check if Key Exists--')
# To determine if a specified key is present in a dictionary use the in keyword:
check_key = 'username'
if check_key in sw2:
    print('Yes, ' + check_key + ' is one of the keys in the sw2 dictionary.')
else:
    print(check_key + ' Is not a key of the sw2 dictionary.')

print('\n--Dictionary Length--')
# To determine how many items (key-value pairs) a dictionary has, use the len() function.
dic_length = len(sw2)
print('Dictionary length: ' + str(dic_length))

print('\n--Adding Items--')
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
sw2['model'] = '6500'
print(sw2)

print('\n--Removing Items--')
# There are several methods to remove items from a dictionary:
# The pop() method removes the item with the specified key name:
sw2.pop('model')
print(sw2)
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
sw2.popitem()
print(sw2)
# The del keyword removes the item with the specified key name:
del sw2['username']
print(sw2)
# The del keyword can also delete the dictionary completely:
# del sw2
# print(sw2)
# The clear() method empties the dictionary:
# sw2.clear()
# print(sw2)

print('\n--Copy a Dictionary--')
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1,
# and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().
sw3 = sw2.copy()
print(sw3)
# Another way to make a copy is to use the built-in function dict().
sw4 = dict(sw3)
print(sw4)

print('\n--Nested Dictionaries--')
# A dictionary can also contain many dictionaries, this is called nested dictionaries.
# Create a dictionary that contain three dictionaries:
all_devices = {
    'rt1': {
        'device_type': 'cisco_ios',
        'host': '192.168.122.91',
        'username': 'admin',
        'password': 'cisco',
    },
    'rt2': {
        'device_type': 'cisco_ios',
        'host': '192.168.122.92',
        'username': 'admin',
        'password': 'cisco',
    }
}
print(all_devices)
# Or, if you want to nest three dictionaries that already exists as dictionaries:
# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
rt1 = {
    'device_type': 'cisco_ios',
    'host': '192.168.122.91',
    'username': 'admin',
    'password': 'cisco',
}
rt2 = {
    'device_type': 'cisco_ios',
    'host': '192.168.122.92',
    'username': 'admin',
    'password': 'cisco',
}
all_devices = {
    'device1' : rt1,
    'device2' : rt2
}
print(all_devices)

print('\n--The dict() Constructor--')
# It is also possible to use the dict() constructor to make a new dictionary:
fw1 = dict(device_type='cisco_asa', host='1.1.1.1', username='cisco', password='cisco')
print(fw1)

# Dictionary Methods
# Python has a set of built-in methods that you can use on dictionaries.
#
# Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key.
#   If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary
