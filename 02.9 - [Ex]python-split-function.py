txt = "hello, my name is Peter, I am 26 years old"

x = txt.split(", ")

print(x)
print(type(x))
print(x[0])

# Get device's IP addresses and desirable system names from file
with open('02.9 - [aux]myalcatels') as file:
    devices = file.read().splitlines()

for i in devices:
    # The device dictionary will be edited each time the for loop runs with the IP addresses from the opened file
    print('I = ' + i)
    if i:
        items = i.split(',')
        device_ip = items[0]
        device_sys_name = items[1]
        print(device_ip)
        print(device_sys_name)
    else:
        print('BREAK!')
        break
