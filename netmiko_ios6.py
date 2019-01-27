#!/usr/bin/env python
from getpass import getpass
from netmiko import Netmiko
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

# Collect login credentials
username = raw_input('Enter your SSH username: ')
password = getpass()

# Sending device ip's stored in a file
with open('devices_list') as f:
    devices_list = f.read().splitlines()

# Iterate through device list and configure the devices
for devices in devices_list:
    print 'Connecting to device ' + devices
    ip_address_of_device = devices
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': username,
        'password': password
    }
    # Error handling parameters
    try:
        net_connect = Netmiko(**ios_device)
    except (AuthenticationException):
        print 'Authentication failure: ' + ip_address_of_device
        continue
    except (NetMikoTimeoutException):
        print 'Timeout to device: ' + ip_address_of_device
        continue
    except (EOFError):
        print "End of file while attempting device " + ip_address_of_device
        continue
    except (SSHException):
        print 'SSH Issue. Are you sure SSH is enabled? ' + ip_address_of_device
        continue
    except Exception as unknown_error:
        print 'Some other error: ' + str(unknown_error)
        continue

    # Configure the device and save config
    output = net_connect.send_config_from_file('more_config')
    output += net_connect.send_command('wr mem\n')
    print output
