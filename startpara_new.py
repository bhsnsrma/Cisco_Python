#!/usr/bin/python3

import paramiko,time,sys

#using as ssh client
client=paramiko.SSHClient()
#auto adjut host kue verification with yes or no
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#time to connect to remote Cisco IOS
addr=sys.argv[1]  # first argument as IP
u=sys.argv[2] #username as 2nd argument
p=sys.argv[3] # password as 3rd argument
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

