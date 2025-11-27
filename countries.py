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
b1=f.getvalue("b1")
try:
 if(b1=="Save"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['countries']
   a=0
   for x in collection.find({}):
    if(t1==x['country_id']):
     a=1
     break
   if(a==1): 
    print("<script>alert('Country Id already exist')</script>")
   else:
    insert1={'country_id':t1,'country_nm':t2,'region_id':t3}
    collection.insert_one(insert1)
    print("<script>alert('Record Saved...')</script>")
    print("<script>window.open('Countries.html','_self')</script>")
 if(b1=="Delete"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['countries']
   delete1={'country_id':t1}
   collection.delete_many(delete1)
   print("<script>alert('Record Deleted...')</script>")
   print("<script>window.open('Countries.html','_self')</script>")
 '''To All Search'''
 if(b1=="All Search"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['countries']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Country id</th><th>Country Name</th><th>Region Id</th></tr>")
   for x in collection.find({}):
    print("<tr><th>",x["country_id"],"</th>","<th>",x["country_nm"],"</th>","<th>",x["region_id"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")
 '''To particular search'''
 if(b1=="PSearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['countries']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Country id</th><th>Country Name</th><th>Region Id</th></tr>")
   for x in collection.find({'country_id':t1}):
    print("<tr><th>",x["country_id"],"</th>","<th>",x["country_nm"],"</th>","<th>",x["region_id"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")
 if(b1=="Update"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['countries']
   collection.update_many({'country_id':t1},{'$set':{'country_nm':t2,'region_id':t3}})
   print("<script>alert('Record Updated...')</script>")
except Exception:
        traceback.print_exc()
