#!/usr/bin/python

import commands
import sys
total=len(sys.argv)
cmdargs=str(sys.argv)

x=[]

for arg in sys.argv:
       x.append(arg)
name=x[1]

#x=commands.getstatusoutput("sudo echo \"/media/"+name+"  *[rw,sync,no_root_squash]\">>/etc/exports")
y=commands.getstatusoutput("sudo echo \"<target "+name+">\n  backing-store  /dev/cloud/"+name+"\n </target>\">>/etc/tgt/targets.conf")

if y[0]==0:
         x=commands.getstatusoutput("sudo systemctl restart tgtd")
         if x[0]==0:
                  print "success"
else :
      print "y" 
        




