#!/usr/bin/env python
#^this thing is called the "shebang"

import os, json, cgi, Cookie

form = cgi.FieldStorage()

username = form.getvalue('user')
password = form.getvalue('password')

C = Cookie.SimpleCookie()
C.load(os.environ['HTTP_COOKIE'])
print "Content-Type: text/html"
if username == "bob" and password =="hunter2":
	print "Set-Cookie: loggedin=true"

print 
print "<HTML><BODY>"
print "<H1>Hello world!</H1>"
print "Your Magic tracking number is:" 
print form.getvalue('magic_tracking_number')
print "<p>Your Browser is"
if "Firefox" in os.environ['HTTP_USER_AGENT']:
	print "firefox!"
elif "Chrome" in os.environ['HTTP_USER_AGENT']:
	print "Chrome!"
else:
	print os.environ['HTTP_USER_AGENT']

print "<FORM method = 'POST'><INPUT name='user'><INPUT name = 'password' type = 'password'>"
print "<INPUT type='submit'></FORM>"

username = form.getvalue('user')
password = form.getvalue('password')
print "<P>Username: " + str(username)
print "<P>Password: " + str(password)
if username == "bob" and password =="hunter2":
	print "<p>Login Success!"

if 'loggedin' in C:
	print "<P>Logged in: " +str(C['loggedin'].value)
else:
	print "<P>No cookie"
#print json.dumps(dict(os.environ), indent=2, sort_keys =True)
