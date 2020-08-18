import getpass
import telnetlib

# Open a file called myswitches which contains the IP addresses of the SWs we are going to configure
file = open('myswitches')

# Ask for username and password
user = input('Enter your telnet username: ')
print('Enter your password: ')
password = getpass.getpass()
print('Enter your enable password: ')
enable_password = getpass.getpass()

first_vlan = ''
last_vlan = ''
prefix_vlan = ''
menu = 'n'
while menu == 'n':

    # Ask for VLANs
    first_vlan = int(input('Enter the first VLAN to create: '))
    last_vlan = int(input('Enter the last VLAN to create: '))
    # Use int(input()) to convert the entered text to int
    # Ask for a prefix for VLAN names
    prefix_vlan = input('Enter the prefix for the VLAN name: ')

    print('The following VLANs will be created: ')
    for n in range(first_vlan, last_vlan + 1):
        print(prefix_vlan + str(n))

    menu = input('Is this OK? (y/n)')

for IP in file:
    print('Configuring SW ' + IP.strip() + '...')
    # The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
    # (space is the default leading character to remove)

    tn = telnetlib.Telnet(IP)
    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')

    if password:
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b'\n')

    if enable_password:
        # If the user has privilege level 15 this won't be needed
        tn.write(b'enable\n')
        tn.write(enable_password.encode('ascii') + b'\n')

    tn.write(b'conf t\n')

    for n in range(first_vlan, last_vlan + 1):
        tn.write(b'vlan ' + str(n).encode('ascii') + b'\n')
        tn.write(b'name ' + prefix_vlan.encode('ascii') + str(n).encode('ascii') + b'\n')

    tn.write(b'end\n')
    tn.write(b'exit\n')

    print(tn.read_all().decode('ascii'))
