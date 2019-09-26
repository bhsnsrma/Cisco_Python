#!/usr/bin/python3

from napalm import get_network_driver
driver=get_network_driver('ios')
##connecting to devicec
device=driver('192.168.176.128','root','cisco')
print([i for i in dir(device) if 'load' in i])
#open session with device
device.open()
#merging config
#only copy config file to router using scp
device.load_merge_candidate(filename='myrouter.txt')
#check the diff in cofig send and config pasted there
print(device.compare_config())
#Commiting the device configuration
c=input("Confirm with Y/N to apply the cconfiguration :")

if c=='y' or c=='Y' :
    print("Commiting the configuration :")
    device.commit_config()
    res=input("Do you want to Rollback the changes : Y/N : ")
    if res=='y' or res=='Y' :
        device.rollback()
        print('Rollback Applied')
    else :
        print ('No Rollback Applied')
elif c=='n' or c=='N' :
    print('Discarding configuration')
    device.discard_config()
else:
    print('please type ony y or n')

# if in case you want to rollback after commiting
#device.rollback()


#close connection as well
device.close()

