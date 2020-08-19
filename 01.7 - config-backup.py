import getpass
import telnetlib

# Open a file called 01.5 - [aux]myswitches which contains the IP addresses of the SWs we are going to configure
file = open('01.5 - [aux]myswitches')

# Ask for username and password
user = input('Enter your telnet username: ')
print('Enter your password: ')
password = getpass.getpass()
print('Enter your enable password: ')
enable_password = getpass.getpass()

for IP in file:
    print('Getting running config from SW ' + IP.strip() + '...')
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

    tn.write(b'terminal length 0\n')
    # terminal length 0 is used to disable the terminal pager
    tn.write(b'show run\n')
    tn.write(b'exit\n')

    read_output = tn.read_all()
    save_output = open('switch_' + IP.strip() + '.conf', 'w')
    # To create a new file in Python, we use the open() method, with one of the following parameters:
    # "x" - Create - will create a file, returns an error if the file exist
    # "a" or "w" - Append or Write - will create a file if the specified file does not exist
    # To write to an existing file, the "a" and "w" parameters should be used with the open() function:
    # "a" - Append - will append to the end of the file
    # "w" - Write - will overwrite any existing content
    save_output.write(read_output.decode('ascii'))
    save_output.write('\n')
    save_output.close()
    print(tn.read_all().decode('ascii'))
