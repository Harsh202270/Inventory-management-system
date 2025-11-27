#!C:/Users/python/AppData/Local/Programs/Python/Python311/python
print("Content-Type:text/html")
print()
import cgi
import traceback
from pymongo import MongoClient
import pymongo
f=cgi.FieldStorage()
t1=f.getvalue("t1")
t2=f.getvalue("t2")
b1=f.getvalue("b1")
client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client['inventory']
collection=db['AgentLogin']
try:
 if(b1=="Log in"):
   a=0
   for x in collection.find({}):
    if(t1==x['id']):
      if(t2==x['password']):
        a=1
        break
   if(a==1): 
    print("<script>window.open('create.html','_self')</script>")
   else:
    print("<script>alert('Either user id or password is wrong....')</script>")
    print("<script>window.open('AgentLogin.html','_self')</script>")
except Exception:
        traceback.print_exc()
