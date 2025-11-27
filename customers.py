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
b1=f.getvalue("b1")
try:
 if(b1=="Save"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['customers']
   insert1={'cus_id':t1,'cus_nm':t2,'cadd':t3,'cweb':t4,'climit':t5}
   collection.insert_one(insert1)
   print("<script>alert('Record Saved...')</script>")
   print("<script>window.open('Customers.html','_self')</script>")
except Exception:
        traceback.print_exc()
