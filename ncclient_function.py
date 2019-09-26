#!/usr/bin/python3

from ncclient import manager
#this code will act as  a netconf client
#using connect function with manager to connect :  Netconfis enabled device
device=manager.connect(host='192.168.176.128',username='root',password='cisco',port=22,allow_agent=False,look_for_keys=False,hostkey_verify=False))
print(device)
print('________________________________')
print('                                ')
time.sleep(2)
print(dir(device))
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
time.sleep()
print(device.get_config('running.data_xml'))

