#!/usr/bin/python

import os,sys,commands
x=[]
for arg in sys.argv:
       x.append(arg)

name=x[1]
size=x[2]
typ=x[3]
ram=x[4]
vcpu=x[5]
e=commands.getstatusoutput("virt-install --vnc --vncport=5913 --vnclisten=0.0.0.0 --name "+name+" --ram "+ram+" --vcpu "+vcpu+" --cdrom /root/Desktop/kali-linux-2.0-i386.iso --disk path=/iaas/"+name+"os.qcow2 --os-type linux --noautoconsole ")
print e



