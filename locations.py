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
   collection=db['location']
   a=0
   for x in collection.find({}):
    if(t1==x['location_id']):
     a=1
     break
   if(a==1): 
    print("<script>alert('Location Id already exist')</script>")
   else:
    insert1={'location_id':t1,'addresh':t2,'postal_code':t3,'city':t4,'state':t5,'country_id':t6}
    collection.insert_one(insert1)
    print("<script>alert('Record Saved...')</script>")
    print("<script>window.open('Locations.html','_self')</script>")
 if(b1=="Delete"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['location']
   delete1={'location_id':t1}
   collection.delete_many(delete1)
   print("<script>alert('Record Deleted...')</script>")
   print("<script>window.open('Locations.html','_self')</script>")
 '''To All Search'''
 if(b1=="All Search"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['location']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Location Id</th><th>Addresh</th><th>Postal Code</th><th>City</th><th>State</th><th>Country Id</th></tr>")
   for x in collection.find({}):
    print("<tr><th>",x["location_id"],"</th>","<th>",x["addresh"],"</th>","<th>",x["postal_code"],"</th>","<th>",x["city"],"</th>","<th>",x["state"],"</th>","<th>",x["country_id"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")
 '''To particular search'''
 if(b1=="PSearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['location']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Location Id</th><th>Addresh</th><th>Postal Code</th><th>City</th><th>State</th><th>Country Id</th></tr>")
   for x in collection.find({'location_id':t1}):
    print("<tr><th>",x["location_id"],"</th>","<th>",x["addresh"],"</th>","<th>",x["postal_code"],"</th>","<th>",x["city"],"</th>","<th>",x["state"],"</th>","<th>",x["country_id"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")
 if(b1=="Update"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['location']
   collection.update_many({'location_id':t1},{'$set':{'addresh':t2,'postal_code':t3,'city':t4,'state':t5,'country_id':t6}})
   print("<script>alert('Record Updated...')</script>")
except Exception:
        traceback.print_exc()
