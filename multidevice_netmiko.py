#!/usr/bin/python3

import netmiko
#multi vendor liberary

device1={
        'username' : 'root',
        'password' : 'cisco',
        'device_type' : 'cisco_ios',
        'host' : '192.168.176.128'
        }


device2={
        'username' : 'root',
        'password' : 'cisco',
        'device_type' : 'cisco_ios',
        'host' : '192.168.176.128'
        }


device3={
        'username' : 'root',
        'password' : 'cisco',
        'device_type' : 'cisco_ios',
        'host' : '192.168.176.128'
        }

# if we pass (**Device1) = it means we are passing dictionary, if we want to pass list then (*Device) 
for i in [device1,device2,device3]:
    device_connect=netmiko.ConnectHandler(**i)
#sending command
    print('Connecting with device type : ->>>',i['device_type'])
    print('Router IP is : ->>>',i['host'])
    print('                                               ')
    output=device_connect.send_command('show ip int br')
    print(output)
    print('**********************************************')

