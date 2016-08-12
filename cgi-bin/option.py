#!/usr/bin/python
"""---------------------------------the file to offer services as options to the user-------------------------"""
print "Content-type:text/html\n"
import cgi,os,commands

"""---------------------function definitions----------------------------"""
#to select parameters for storage as a service
def staas():
        print """
            <form action="project/staas.py" method="GET">
            name:<input type ='text' name='nm'>
            size:<input type='text' name='sz'>
            <input type='submit' value='submit'>
            </form>      
              """
        
#to selct parameters for infrastructure as a service                 
def iaas():
        print """
            <form action="project/iaas.py" method="GET">
            name :<input type ='text' name='nm'><br>
            os-type:
            <select name='ty'>
            <option value="linux">LINUX</option>
            <option value="windows">WINDOWS</options>
            </select><br>
            size of hard disk:<input type='text' name='sz'><br>
            enter the os-variant:<input type='text' name='vt'><br>
            enter the ram size:<input type='text' name='ram'><br>
            enter the  no of cpus:
            <select name ='vcpu'>
            <option value='1'>1</option>
            <option value='2'>2</option>
            </select> <br>
            <input type='submit' value='submit'>
            </form>      
              """ 
           
#to select parameters for software as a service           
def saas():
         print """
            <form action="project/saas.py" method="GET">
            enter the name of s/w you wanna use:<input type ='text' name='nm'>
            <input type='submit' value='submit'>
            </form>      
              """
#to offer container as a service but still in progress
def caas():
        print """
              <html>
<head>
<style>
div.ubuntu{
position : absolute;
left:100px;
top:100px;
}
div.fedora{
position :absolute; 
left :500px;
top :100px;

}
</style>
</head>

<div class="ubuntu">

<form method="POST" action="project/caas.py">
<input type ="hidden" name="python" value="0">
<input type="hidden" name="gcc" value="0">
<input type="hidden" name="nginx" value="0">
<input type="hidden" name="ruby" value="0">
<em><b>ubuntu</b></em><input type ="radio" name="os" value="ubuntu"><br>
version<select name="version">
<option value="14.04">14.04</option>
</select><br>
python<input type ="checkbox" value ="python" name="python" ><br>
nginx<input type ="checkbox" value ="nginx" name="nginx" ><br>
gcc<input type ="checkbox" value ="gcc" name="gcc" ><br>
ruby<input type ="checkbox" value ="ruby" name="ruby" ><br>
<input type ="submit" value="submit">
</form>
</div>

<div class="fedora">

<form method="GET" action="project/saas.py">
<input type ="hidden" name="python" value="0">
<input type="hidden" name="gcc" value="0">
<input type="hidden" name="nginx" value="0">
<input type="hidden" name="ruby" value="0">

<em><b>fedora</b></em><input type="radio" name ="os" value="fedora"><br>
version<select name="version">
<option value="14.04">14.04</option>
</select><br>
python<input type ="checkbox" value ="python" name="python" ><br>
nginx<input type ="checkbox" value ="nginx" name="nginx" ><br>
gcc<input type ="checkbox" value ="gcc" name="gcc" ><br>
ruby<input type ="checkbox" value ="ruby" name="ruby" ><br>
<input type ="submit" value="submit">
</form>
</div>

</html>
              """        

data=cgi.FormContent()
value=data['input'][0]
print value


#to select the required service
if(value=='1'):
        staas()
elif(value=='2'):
            saas()
elif(value=='3'):
            iaas() 
elif(value=='4'):
             caas()  
else :
     print "not a valid option"

