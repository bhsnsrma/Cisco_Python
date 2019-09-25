#!/usr/bin/python3

import netmiko
#multi vendor liberary
from getpass import getpass
sec=getpass('Please Enter password for the device :')  # getting password without showing the characters.

device1={
        'username' : 'root',
        'password' : sec,
        'device_type' : 'cisco_ios',
        'host' : '192.168.176.128'
        }


device2={
        'username' : 'root',
        'password' : sec,
        'device_type' : 'cisco_ios',
        'host' : '192.168.176.128'
        }


device3={
        'username' : 'root',
        'password' : sec,
        'device_type' : 'cisco_ios',
        'host' : '192.168.176.128'
        }

# if we pass (**Device1) = it means we are passing dictionary, if we want to pass list then (*Device) 
for i in [device1,device2,device3]:
    try :
        device_connect=netmiko.ConnectHandler(**i)   #sending command
        print('**********************************************')
        print('Connecting with device type : ->>>',i['device_type'])
        print('Router IP is : ->>>',i['host'])
        print('                                               ')
        output=device_connect.send_command('show ip int br')
        print(output)
        print('**********************************************')
    except netmiko.ssh_exception.NetMikoTimeoutException :
        print('Please check you network ip :',i['host'])
    except netmiko.ssh_exception.NetMikoAuthenticationException :
        print('Wrong username or password for host : ',i['host'])
    except :
        print('Please check the Device_Type or Host details in Code',i['host'])


