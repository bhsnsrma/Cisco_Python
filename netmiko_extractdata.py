#!/usr/bin/python3

import netmiko,time
#multi vendor liberary

device1={
        'username' : 'root',
        'password' : 'cisco',
        'device_type' : 'cisco_ios',
        'host' : '192.168.176.128'
        }

#print([i for i in dir(device_connect) if 'send' in i])
#now sending config from file]
device_connect = netmiko.ConnectHandler(**device1)
#print(output)
#sending config from file
output1=device_connect.send_command('show ip int br')
output=device_connect.send_command('show ip int br', use_textfsm=True)
print(output)
print(output1)
for i in output:
    print('my interface bame is ',i['intf'], 'with IP',i['ipaddr'],'having status up',i['status'])
    time.sleep(1)
