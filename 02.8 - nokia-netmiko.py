from netmiko import ConnectHandler

# device = dict(device_type='cisco_ios', host=IP.strip(), username='admin', password='cisco')
device = dict(device_type='alcatel_sros', host='192.168.122.100', username='admin', password='admin')
net_connect = ConnectHandler(**device)
print('\nConfiguring system name on ' + device['host'] + '...')
# output = net_connect.send_command('show bof')
config_set = ['configure system name R1',
              'admin save']
output = net_connect.send_config_set(config_set)
print(output)
