#!/usr/bin/python3
from subprocess import getoutput,check_output
import sys
import os
data=sys.argv[1:]

for i in data :
    print("PING REQUEST FOR SERVER : " +i)
    print(os.system("ping -c 3 "+i))
    print("-----------------------")
    print("-----------------------")

