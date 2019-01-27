#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass

# SSH username and password provided by user
username = raw_input('Enter your SSH username: ')
password = getpass()

# Sending device ip's stored in a file 
with open('devices_list') as f:
    devices_list = f.read().splitlines()

# Iterate through device list and configure the devices 
for devices in devices_list:
    print 'Connecting to device ' + devices
    ip_address_of_device = devices
    
    # SSH Connection details
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device, 
        'username': username,
        'password': password
    }
 
    net_connect = Netmiko(**ios_device)
    output = net_connect.send_config_from_file('more_config')
    print output
