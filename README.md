# CLOUD #


### What is this repository for? ###
*This repository is used to host files required to create and provide cloud services.
*The cloud can provide services namely IAAS,STAAS and SAAS.
*This is the first version of software.**(Version 1.0)**


### How do I get set up? ###

##Prerequisites:##
   *The above cloud can be hosted only on **redhat** distribution of Linux operating system.
   *The client also is supposed to be running the redhat distribution of the Linux operating system.
   *The yum repository should be enabled on the redhat.The instructions to enable the yum repository are given on the link :https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Deployment_Guide/sec-Configuring_Yum_and_Yum_Repositories.html

##setup:##

In order to deploy your own cloud the following steps are required to be followed:-
* login into the root account of the redhat . 
* download or clone the repository.
* Place the files in **cgi-bin** folder to the **cgi-bin** folder in the location **/var/www/cgi-bin** of your **root** account.
* place the files in **html** folder to the **html** folder in the location **/var/www/html** of your **root** account.
* place the **writing_files** folder into **Desktop** of the **root** account in the location **/root/Desktop**
* restart the web-server ,i.e.,the apache http server using the command "systemctl restart httpd"
* Disable the firewall using the coomand **"setenforce 0"** && **"iptables -F"**
   ----------------------the cloud is ready to serve------------------------------

###Configuration###

 ##web-server##
   *Grant the sudo access to apache web server by repacing the line with the keyword "Apache" with the following line:-
       %Apache        ALL=(ALL)       ALL
   *Run the command: #>systemctl restart httpd
 
 ##SSH-server##
   *Run the command: #>yum install openssh-server
   *After installation open /etc/ssh/sshd_config in vim editor and replace the line with keyword **"X11Forwarding"** with:-
      X11Forwarding yes

 ##proxifier##
   *Download the websockify software from:https://github.com/kanaka/websockify
   *Inside the folder run the following command:-
    " ./run :#port_no 127.0.0.1:#vnc_port "(where the #port_no is the port where we run the proxifier && #vnc_port is the port on which the vnc is listening.)
   
    
 ##others##     
   *All the other services dont need any configuration changes.

###Dependencies###

* OS : **REDHAT 7.2**  distribution of **Linux**
* Services : **iscsi,ssh,MySQL,APACHE (httpd)**.
* Softwares : **websockify**,**noVNC**,**qemu-kvm**,**python 2.7**,**MongoDB**.
* Packages : **pymysql**,**os**,**commands**,**cgi**. 

###How it works###

##Registration##
  *The user is supposed to register by providing the details as per asked by the register.html page inside the folder "html"
  *The details  of user is passed to register.py which registers the new user to database.Register.py is inside the folder cgi-bin .
  * **Register.py** takes in the input from user and redirects to option.py in the folder cgi-bin/option.py


##login##
  *If the user is already registered then he can login via the login.html page inside the folder "html"
  *If the user provides the correct credentials then the user is redirected to the **login_server.py** file otherwise is asked to register via the **register.html**.
  ***login_server.py** takes in the input from user and redirects to **option.py**.
    
##option.py##
   *This file transfers the control to the following files according to he option selected by the user:-
     a)**staas.py**
     b)**saas.py**
     c)**iaas.py**
   
##staas.py##

   *It takes in the input provided by the user as per requirements of the user. 
   *This file creates a logical volume in the server of size desired by the user.
   *It then passes control to **a.py** inside the folder "writing_files/a.py".It creates a pyhton script for the user to download.
   *The control returns to staas.py and the user is made to download the pytHon file created by **a.py**.
   *The user has to run the script by double-clicking the script .
   *Thus a new block device appears into the system of the user .The user can check it via the command "fdisk -l"
   *The user has to mount the block-device in order to make use of it.
   
##saas.py##

   *It takes in the input provided by the user as per requirements of the user. 
   *It then passes control to **c.py** inside the folder "writing_files/c.py".It creates a pyhton script for the user to download.
   *The control returns to saas.py and the user is made to download the pytHon file created by **c.py**.
   *The user has to run the script by double-clicking the script .
   *Thus a console of the requested software appears on the screen of the user.

##iaas.py##

   *It takes in the input provided by the user as per requirements of the user. 
   *It then passes control to **d.py** inside the folder "writing_files/d.py".
   ***d.py** creates a new virtual os of the specifications requested by the user.
   *The user is made to redirect to the noVNC page where the user has to enter the ip_address of the server and the port number where the websockify is running.
   *Thus after this the console of the new os appears on the browser.
   

### Who do I talk to? ###
* Aman Sinha (amansinha1412@gmail.com)