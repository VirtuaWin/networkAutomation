from netmiko import ConnectHandler

# Get device's IP addresses and desirable system names from file
with open('myalcatels') as file:
    devices = file.read().splitlines()

for i in devices:
    # The if statement (in conjunction with the else statement) makes sure there is something in the i variable
    # to avoid trying to get data from an empty variable, which would happen if the file has empty lines
    # In other words, if i is empty, it means we are reading an empty line, so we break out of the for loop
    if i:
        # The device dictionary will be edited each time the for loop runs with the IP addresses from the opened file
        # print('i = ' + i)
        items = i.split(',')
        device_ip = items[0]
        device_sys_name = items[1]
        device = dict(device_type='alcatel_sros', host=device_ip, username='admin', password='admin')
        # .strip() is used to remove new lines (\n)
        # Establish an SSH connection to the device by passing in the device dictionary.
        net_connect = ConnectHandler(**device)
        print('Configuring device ' + str(device['host']) + '...')  # Get the device's IP address from de dictionary
        config_commands = ['configure system name ' + device_sys_name,
                           'admin save']
        output = net_connect.send_config_set(config_commands)
        print(output)
    else:
        break

print('\nDONE!\n')
