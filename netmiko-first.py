from netmiko import ConnectHandler

# Create a dictionary representing the device.
# Supported device_types can be found in ssh_dispatcher.py, see CLASS_MAPPER keys.
sw = {
    'device_type': 'cisco_ios',
    'host': '192.168.122.92',
    'username': 'admin',
    'password': 'cisco',
    # 'port': 8022,  # optional, defaults to 22
    # 'secret': 'cisco',  # optional, defaults to ''
}

# Establish an SSH connection to the device by passing in the device dictionary.
net_connect = ConnectHandler(**sw)

# Execute show commands with the send_command function.
output = net_connect.send_command('show ip int brief')
print(output)

# Execute configuration change commands with the send_config_set function (will automatically enter into config mode)
config_commands = ['int loop 0',
                   'ip address 2.2.2.2 255.255.255.0',
                   'no shut']
output = net_connect.send_config_set(config_commands)
print(output)

for n in range(71, 81):
    print('Creating VLAN Netmiko_VLAN_' + str(n))
    config_commands = ['vlan ' + str(n),
                       'name Netmiko_VLAN_' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print(output)
