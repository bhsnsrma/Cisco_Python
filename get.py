#!/usr/bin/python3

from time import ctime,sleep
#only importing specific functions
from subprocess import  getstatusoutput,getoutput,check_output
from os import mkdir

options='''
press 1 to check current date and time
press 2 to run any command in your cueenrt os :
press 3 to create a directory :
press 4 to start a train :
press 5 ping any website :
'''

print(options)
# to capture input from user
choice=input()
print("You have choosen",choice)

#conditional statement

if choice== '1' :
    print(ctime())
elif int(choice) == 2 :
    cmd=input("Please enter any command : ")
    output=getoutput(cmd)
    print(output)
elif choice == '3' :
     d_name=input("Enter Dir name to create : ")
     mkdir(d_name)
     print(d_name," Successfully Created ")
     # HOMEWORK
elif choice == '5':
    web=input ("Enter the WEBSITE name : ")
    print(getoutput("ping -c 5 "+web))
else:
    print("wrong option")


