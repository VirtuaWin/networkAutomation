# Get configuration commands from a file
with open('02.4 - [aux]iou-l2-campus-cisco-design') as file:
    lines = file.read().splitlines()
print(lines)

# In Python you need to give access to a file by opening it. You can do it by using the open() function.
# Open returns a file object, which has methods and attributes for getting information about and manipulating
# the opened file.
# With the “With” statement, you get better syntax and exceptions handling.
# In addition, it will automatically close the file. The with statement provides a way for ensuring that
# a clean-up is always used.
# Opening a file using with is as simple as: with open(filename) as file:

# with open('02.9 - [aux]myalcatels') as file:
#     devices = file.read().strip()
# print(devices)
