#!/usr/bin/python3

import paramiko,time

#using as ssh client
client=paramiko.SSHClient()
#auto adjut host kue verification with yes or no
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#time to connect to remote Cisco IOS
addr=input("Enter your Router IP :")
u='root'
p='cisco'
#connected with SSh session
client.connect(addr,username=u,password=p,allow_agent=False, look_for_keys=False)
#we have to ask for shell
device_access=client.invoke_shell()
#now sending command
device_access.send("show ip int br \n")
time.sleep(1)
## assuming command got executed, receive data.
output=device_access.recv(65000)
#deconding byte - like string into staring
print(output.decode('ascii'))

