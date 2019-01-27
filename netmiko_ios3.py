#!/usr/bin/env python
from netmiko import Netmiko

# Sending multiple lines of config stored in a file 
#with open('basic_config') as f:
#    commands_to_send = f.read().splitlines()

# SSH Connection details 
ios1 = {
    'device_type': 'cisco_ios',
    'ip': '172.21.56.120',
    'username': 'cisco',
    'password': 'cisco',
}
 
all_devices = [ios1]

# Iterate through device list and configure the devices  
for devices in all_devices:
    net_connect = Netmiko(**devices)
    output = net_connect.send_config_from_file('basic_config')
    print output
