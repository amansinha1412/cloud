#!/usr/bin/python
print "Content-type:text/html\n"
import os,commands,cgi
data=cgi.FormContent()
soft=data['nm'][0]

p="echo qwerty | sudo -S "                 
#a=commands.getstatusoutput("echo qwerty | sudo -S lvcreate --size "+ size +"K --name "+ name +" cloud")
#b=commands.getstatusoutput(p +"mkdir /media/"+name)
#c=commands.getstatusoutput(p+"chmod 777 /media/"+name)
#d=commands.getstatusoutput(p +"mkfs.ext4 /dev/cloud/"+name )
#e=commands.getstatusoutput(p + "mount /dev/cloud/"+name+ " /media/"+name)
#y=commands.getstatusoutput(p+"echo /dev/cloud/"+name+" /media/"+name+ " ext4 defaults 0 0  >>etc/fstab")
#os.system(p+"echo /dev/cloud/"+name+" /media/"+name+ " ext4 defaults 0 0  >>etc/fstab")
#f=commands.getstatusoutput("sudo echo '/media/"+name+ "  *[rw,sync,no_root_squash]' >> /etc/exports" )
#print f
#-------------to write in the export file------------------------(/root/Desktop/a.py is used)
g=commands.getstatusoutput(p+"python /root/Desktop/writing_files/c.py " +soft)
if g[0]==0:
         print "success"
         print "<a href=\"http://localhost/"+soft+".tar\">click here</a>"   
         #i=commands.getstatusoutput(p + "python /root/Desktop/writing_files/b.py "+name)
         #print i
         #if i[0]==0:
                 #print"<meta HTTP-EQUIV=\"refresh\" CONTENT=0; ,URL=\"http://192.168.43.68/"+name+".tar\">"
else :
     print "iaas-error"
