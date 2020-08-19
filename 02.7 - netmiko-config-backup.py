from netmiko import ConnectHandler
import datetime

file = open('myswitches')

for IP in file:
    # device = dict(device_type='cisco_ios', host=IP.strip(), username='admin', password='cisco')
    device = dict(device_type='cisco_ios', host=IP.strip(), username='admin', password='cisco')
    net_connect = ConnectHandler(**device)
    print('\nGetting configuration from ' + IP.strip() + '...')
    output = net_connect.send_command('show run')

    # Get current time
    date = datetime.datetime.now().strftime('%d-%m-%Y_%X')
    # Save configuration to file
    conf_file = 'netmiko_switch_' + IP.strip() + '_' + date + '.conf'
    save_output = open(conf_file, 'w')
    save_output.write(output)
    save_output.write('\n')
    save_output.close()

    print('File saved as ' + conf_file)
