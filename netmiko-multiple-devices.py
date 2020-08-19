from netmiko import ConnectHandler

# Create a dictionary representing each device.
# Supported device_types can be found in ssh_dispatcher.py, see CLASS_MAPPER keys.
sw2 = {
    'device_type': 'cisco_ios',
    'host': '192.168.122.92',
    'username': 'admin',
    'password': 'cisco',
    # 'port': 8022,  # optional, defaults to 22
    # 'secret': 'cisco',  # optional, defaults to ''
}
sw3 = {
    'device_type': 'cisco_ios',
    'host': '192.168.122.93',
    'username': 'admin',
    'password': 'cisco',
}
sw4 = {
    'device_type': 'cisco_ios',
    'host': '192.168.122.94',
    'username': 'admin',
    'password': 'cisco',
}
sw5 = {
    'device_type': 'cisco_ios',
    'host': '192.168.122.95',
    'username': 'admin',
    'password': 'cisco',
}
sw6 = {
    'device_type': 'cisco_ios',
    'host': '192.168.122.96',
    'username': 'admin',
    'password': 'cisco',
}

# Define a list with all the devices
all_devices = [sw2, sw3, sw4, sw5, sw6]

# For loop to navigate through the list
for device in all_devices:
    # Establish an SSH connection to the device by passing in the device dictionary.
    net_connect = ConnectHandler(**device)
    print('Configuring device ' + str(device['host']) + '...')  # Get the device's IP address from de dictionary
    for n in range(90, 101):
        config_commands = ['vlan ' + str(n),
                           'name Netmiko_VLAN_' + str(n)]
        output = net_connect.send_config_set(config_commands)
        print(output)

print('\nDONE!\n')
