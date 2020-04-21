import random
import os
import subprocess

def get_random():
    return random.choice("abcdef0123456789")

def new_mac():
    new=" "
    for i in range(0,5):
        new=get_random()+get_random()+ ":"
    new=get_random()+get_random()
    return new
#print the old mac address

print(os.system("ifconfig eth0 | grep ether | grep -oE [0-9abcdef:]{17}"))

#turn eth0 down

subprocess.call(["sudo","ifconfig","eth0","down"]) 

new_m=new_mac()
#assign new mac address

subprocess.call(["sudo","ifconfig","eth0","hw","ether","%s"%new_m]) 
#turn eth0 with the new mac
subprocess.call(["sudo","ifconfig","eth0","up"]) 

#print the new mac address

print(os.system("ifconfig eth0 | grep ether | grep -oE [0-9abcdef:]{17}"))




