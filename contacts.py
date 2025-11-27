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
t3=f.getvalue("t3")
t4=f.getvalue("t4")
t5=f.getvalue("t5")
t6=f.getvalue("t6")
b1=f.getvalue("b1")
try:
 if(b1=="Save"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['contacts']
   a=0
   for x in collection.find({}):
    if(t1==x['contact_id']):
     a=1
     break
   if(a==1): 
    print("<script>alert('Contact Id already exist')</script>")
   else:
    insert1={'contact_id':t1,'first_nm':t2,'last_nm':t3,'email':t4,'phone':t5,'customer_id':t6}
    collection.insert_one(insert1)
    print("<script>alert('Record Saved...')</script>")
    print("<script>window.open('Contacts.html','_self')</script>")
 if(b1=="Delete"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['contacts']
   delete1={'contact_id':t1}
   collection.delete_many(delete1)
   print("<script>alert('Record Deleted...')</script>")
   print("<script>window.open('Contacts.html','_self')</script>")
 '''To All Search'''
 if(b1=="All Search"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['contacts']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Contact id</th><th>First name</th><th>Last name</th><th>Email Id</th><th>Phone no.</th><th>Customer Id</th></tr>")
   for x in collection.find({}):
    print("<tr><th>",x["contact_id"],"</th>","<th>",x["first_nm"],"</th>","<th>",x["last_nm"],"</th>","<th>",x["email"],"</th>","<th>",x["phone"],"</th>","<th>",x["customer_id"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")
 '''To particular search'''
 if(b1=="PSearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['contacts']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Contact id</th><th>First name</th><th>Last name</th><th>Email Id</th><th>Phone no.</th><th>Customer Id</th></tr>")
   for x in collection.find({'contact_id':t1}):
    print("<tr><th>",x["contact_id"],"</th>","<th>",x["first_nm"],"</th>","<th>",x["last_nm"],"</th>","<th>",x["email"],"</th>","<th>",x["phone"],"</th>","<th>",x["customer_id"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")
 if(b1=="Update"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['contacts']
   collection.update_many({'contact_id':t1},{'$set':{'first_nm':t2,'last_nm':t3,'email':t4,'phone':t5,'customer_id':t6}})
   print("<script>alert('Record Updated...')</script>")
except Exception:
        traceback.print_exc()
