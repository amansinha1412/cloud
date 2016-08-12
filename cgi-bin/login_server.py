#!/usr/bin/python
import cgi,commands,pymysql,os
#---------------------------------------------the file for user login-------------------------------------
print "Content-type:text/html\n"



data = cgi.FormContent()

email=data['email'][0]
password=data['password'][0]


#connection to the database:
connection=pymysql.connect(host='localhost',
                            user='root',
                            db='cloud',
                            password='',
                            cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
          sql="SELECT name,password FROM  users WHERE email= %s AND password=%s "
          cursor.execute(sql,(email,password))
          #::to make the changes in the database:::
          result=cursor.fetchone()
          if(result):
                 print "welcome"
                 print "<br>"
                 print """
                       enter 1 : to start the stass service:<br>
                       enter 2 to start the saas service:<br>
                       enter 3 to start the iaas service:<br>
                       <form action="option.py" method="POST">
                       <select name="input">
                       <option valu="1">1</option>
                       <option value="2">2</option>
                       <option value="3">3</option>
                       <option value="4">4</option>
                       </select>
                       <br> 
                       <input type="submit" value="submit">
                       </form>
                       """
         #to make the client register ino the database
         else :
                print """
                          click here to sign up.
                          <br>
                          <a href="register.html">register</a>
                      """
    connection.commit()

finally:
   connection.close()
   

