#!/usr/bin/python

import os,commands,sys
x=[]
for arg in sys.argv:
       x.append(arg)
name=x[1]

os.system("sudo touch /root/Desktop/"+name+".py")
os.system("sudo chmod o+x /root/Desktop/"+name+".py")

f=open("/root/Desktop/"+name+".py","w")
f.write("#!/usr/bin/python")
f.write("\nimport os,commands")

f.write("\nnm="+"\""+name+"\"")
#f.write("\ni=commands.getstatusoutput(\'sudo yum install nfs-utils\')")
f.write("\ni=commands.getstatusoutput(\'sudo yum install iscsi-initiator-utils\')")

#f.write("\nprint i")
f.write("\nprint i")
#f.write("\nf=commands.getstatusoutput(\'sudo mkdir /media/"+name+"\')")
f.write("\nf=commands.getstatusoutput(\'sudo iscsiadm --mode discoverydb --type sendtargets --portal 192.168.43.68 --discover\')")
f.write("\nprint f")
#f.write("\niqn=f[1]")
f.write("\nq=commands.getstatusoutput(\"sudo iscsiadm --mode node --targetname \"+nm+\" --portal 192.168.43.68 --login\")")
f.write("\nprint q")
f.write("\nraw_input()")
f.write("\nos.system(\'sudo mkdir /media/\"+nm+\'")
f.write("\nprint\'mount the hard disk as given in the instructions below:\'")
f.write("\nprint\"remove any pendrive or hard disk\"")
f.write("\nraw_input(\"press enter to continue after removing the disks\")")
f.write("\ncommands.getstatusoutput(\"sudo mkfs.ext4 /dev/sdb\")")
f.write("\ncommands.getstatusoutput(\"sudo mount /media/\"+nm+\" /dev/sdb\")")

#f.write("\nprint f")

#f.write("\ng=commands.getstatusoutput(\'sudo mount 192.168.43.68:/media/"+name+" /media/"+name+"\')")

#f.write("\nprint g")

#f.write("\n sudo gsettings  set org.gnome.nautilus.preferences executable-text-activation  ask")
f.close()
awq=commands.getstatusoutput("sudo tar -cf "+name+".tar /root/Desktop/"+name+".py")

bzs=commands.getstatusoutput("sudo mv "+name+".tar /var/www/html/")
 
