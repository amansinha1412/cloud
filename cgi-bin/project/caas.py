#!/usr/bin/python
print "Content-type:text/html\n"
import os,commands,cgi
print "hi"

data=cgi.FormContent()
os=data['os'][0]
version=data['version'][0]
print os
if (data['python'][0]=="0"):
        python=0
else :
        python=1
if (data['nginx'][0]=="0"):
        nginx=0
else :
        nginx=1
if (data['gcc'][0]=="0"):
        gcc=0
else :
        gcc=1
        
if (data['ruby'][0]=="0"):
        ruby=0
        print "getting here" 
else :
        ruby=1
print python
print os
print gcc
print nginx
print ruby

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
g=commands.getstatusoutput(p+"python /root/Desktop/writing_files/e.py " +os+" "+version+" "+python+" "+nginx+" "+gcc+" "+ruby)
if g[0]==0:
         e=commands.getstatusoutput(p+"systemctl restart docker")
         print e   
         #f=commands.getstatusoutput(p+"docker build -t \"c1\" /dockers")  
         #print f
         #x=commands.getstatusoutput(p+"docker run -d -p 32770:4200 --privileged --name c1 c1")
         #print x"""
         print "good"

         #print "<a href=\"http://localhost/"+soft+".tar\">click here</a>"   
         #i=commands.getstatusoutput(p + "python /root/Desktop/writing_files/b.py "+name)
         #print i
         #if i[0]==0:
                 #print"<meta HTTP-EQUIV=\"refresh\" CONTENT=0; ,URL=\"http://192.168.43.68/"+name+".tar\">"
else :
     print "caas-error"

