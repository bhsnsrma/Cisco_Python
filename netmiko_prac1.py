#!/usr/bin/python3

import netmiko
#multi vendor liberary

device1={
        'username' : 'root',
        'password' : 'cisco',
        'device_type' : 'cisco_ios',
        'host' : '192.168.176.128'
        }

#connect target device
# by cheking couple of things coonect handler will allow you to connect.
'''

        Device type

'''
# if we pass (**Device1) = it means we are passing dictionary, if we want to pass list then (*Device) 
device_connect=netmiko.ConnectHandler(**device1)
#print([i for i in dir(device_connect) if 'send' in i])

#now sending config from file]

output1=device_connect.send_config_from_file('myrouter.txt')
print(output)

