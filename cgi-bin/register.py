#!/usr/bin/python
import cgi,commands,pymysql,os
print "Content-type:text/html\n"



data = cgi.FormContent()

email=data['email'][0]
name=data['name'][0]
password=data['passwd'][0]

#connection to the database:
connection=pymysql.connect(host='localhost',
                            user='root',
                            db='cloud',
                            password='',
                            cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
          #to register the user into the database of the server
          sql="INSERT INTO users (email,password,name) VALUES (%s, %s, %s)"
          result=cursor.execute(sql,(email,password,name))
          #::to make the changes in the database:::
          #to offer the services as options
          if result==1:
                   print "welcome"
                   print "<br>"
                   print """
                       enter 1 to start the stass service:<br>
                       enter 2 to start the saas service:<br>
                       enter 3 to start the iaas service:<br>
                       <form action="option.py" method="POST">
                       <select name="input">
                       <option valu="1">1</option>
                       <option value="2">2</option>
                       <option value="3">3</option>
                       </select><br>
                       <input type='submit' value='submit'>
                       </form>
                       """
          else :
                print """
                          sorry there was server error
                          <br>
                          <a href="register.html">register</a>
                      """
    connection.commit()

finally:
   connection.close()
   

