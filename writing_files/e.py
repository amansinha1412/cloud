#!/usr/bin/python
import os,commands,sys
x=[]
for arg in sys.argv:
       x.append(arg)
os=x[1]
version=x[2]
python=x[3]
nginx=x[4]
gcc=x[5]
ruby=x[6]

print os
print version
print python
print nginx
print gcc
print ruby
#os.system("sudo touch /dockers/Dockerfile")
#os.system("sudo chmod o+x /root/Desktop/writing_files")
if os=="ubuntu":
	f=open("/dockers/Dockerfile","w")
	f.write("FROM cloud_test")
	f.write("\nMAINTAINER amansinha1412@gmail.com")
	f.write("\nRUN apt-get -y install "+python+" "+nginx+" "+gcc+" "+ruby)
        f.write("\nCMD [./start.sh]")
	f.close()

