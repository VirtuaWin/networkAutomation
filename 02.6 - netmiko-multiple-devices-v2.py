from netmiko import ConnectHandler

# Prepare the config commands with the VLANs we want to create
config_commands = []
for n in range(121, 130):
    config_commands = config_commands + ['vlan ' + str(n),
                                         'name Netmiko_VLAN_' + str(n)]
# By doing this we avoid exiting and entering conf t each time a VLAN is created
# This way we create a list with all the VLANs we want to create instead of creating a new list each time
# the for loop runs

# Open a file called myswitches which contains the IP addresses of the SWs we are going to configure
file = open('myswitches')

# Create a dictionary representing each device.
for IP in file:
    # The dictionary device will be edited each time the for loop runs with the IP addresses from the opened file
    device = dict(device_type='cisco_ios', host=IP.strip(), username='admin', password='cisco')
    # .strip() is used to remove new lines (\n)
    # Establish an SSH connection to the device by passing in the device dictionary.
    net_connect = ConnectHandler(**device)
    print('Configuring device ' + str(device['host']) + '...')  # Get the device's IP address from de dictionary
    output = net_connect.send_config_set(config_commands)
    print(output)

print('\nDONE!\n')
