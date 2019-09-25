#!/usr/bin/python3

import paramiko,time,sys

#using as ssh client
client=paramiko.SSHClient()
#auto adjut host kue verification with yes or no
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#create list of devices
device_ip=["192.168.176.128","192.168.176.128","192.168.176.128"]
u='root'
p='cisco'

#Apply the loop
for i in device_ip :
        print("Connect with devices : ",i)
    #connected with SSh session
        client.connect(i,username=u,password=p,allow_agent=False, look_for_keys=False)
    #we have to ask for shell
        device_access=client.invoke_shell()
    #now sending command
        device_access.send("show ip int br \n")
        time.sleep(1)
    ## assuming command got executed, receive data.
        output=device_access.recv(65000)
    #deconding byte - like string into staring
        print(output.decode("ascii"))
    #store file
        with open(i+time.ctime(),'w') as f:
            f.write(output.decode('ascii'))
            time.sleep(1) 


