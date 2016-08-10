#!/usr/bin/python
import commands,cgi,thread
print "Content-type:text/html\n"
#print "hi"
print ""

data=cgi.FormContent()

name=data['nm'][0]
size=data['sz'][0]
typ=data['ty'][0]
ram=data['ram'][0]
vcpus=data['vcpu'][0]
variant=data['vt'][0]

#print name
#print size
#print typ
#print ram
#print vcpus
#print variant
p="echo qwerty | sudo -S "
def myc():
       r=commands.getstatusoutput(p+"python /root/Desktop/writing_files/d.py " +name+" "+size+" "+typ+" "+ram+" "+vcpus)
       #print r           
            

a=commands.getstatusoutput(p+"systemctl restart libvirtd")
#print a
e=commands.getstatusoutput(p+"qemu-img create -f qcow2 /iaas/"+name+"os.qcow2 "+size+"G")
#print e
if e[0]==0:
        print "<a href=\"http://localhost/noVNC-master/vnc.html\">click here</a>" 
        thread.start_new_thread(myc(),())
        
        #print"<meta HTTP-EQUIV=\"refresh\" CONTENT=0; ,URL=\"http://192.168.43.68/noVNC-master/vnc.html\">"
        #e=commands.getstatusoutput(p+"sudo virsh destroy "+name)
        #f=commands.getstatusoutput(p+"sudo virsh start "+name) 
        #print "<meta http-equiv=\"refresh\" content=\"0; URL=http://localhost/noVNC-master/vnc.html\" />"
       
else :
   print "no space on server sorry"

                                             
          
             
 



