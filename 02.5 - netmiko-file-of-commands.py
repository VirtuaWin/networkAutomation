from netmiko import ConnectHandler

# Create a dictionary representing each device.
# Supported device_types can be found in ssh_dispatcher.py, see CLASS_MAPPER keys.
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
all_devices = [sw4, sw5, sw6]

# Get commands from file
with open('02.4 - [aux]iou-l2-campus-cisco-design') as file:
    config_commands = file.read().splitlines()

# For loop to navigate through the list
for device in all_devices:
    # Establish an SSH connection to the device by passing in the device dictionary.
    net_connect = ConnectHandler(**device)
    print('Configuring device ' + str(device['host']) + '...')  # Get the device's IP address from de dictionary
    output = net_connect.send_config_set(config_commands)
    print(output)

print('\nDONE!\n')
