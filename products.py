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
   collection=db['products']
   a=0
   for x in collection.find({}):
    if(t1==x['prod_id']):
     a=1
     break
   if(a==1): 
    print("<script>alert('Product Id already exist')</script>")
   else:
    insert1={'prod_id':t1,'prod_nm':t2,'description':t3,'standard_cost':t4,'Last_price':t5,'category_id':t6}
    collection.insert_one(insert1)
    print("<script>alert('Record Saved...')</script>")
    print("<script>window.open('Products.html','_self')</script>")
 if(b1=="Delete"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['products']
   delete1={'prod_id':t1}
   collection.delete_many(delete1)
   print("<script>alert('Record Deleted...')</script>")
   print("<script>window.open('Products.html','_self')</script>")
 '''To All Search'''
 if(b1=="All Search"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['products']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Product id</th><th>Product name</th><th>Description</th><th>Standard Cost</th><th>Last Price</th><th>Category Id</th></tr>")
   for x in collection.find({}):
    print("<tr><th>",x["prod_id"],"</th>","<th>",x["prod_nm"],"</th>","<th>",x["description"],"</th>","<th>",x["standard_cost"],"</th>","<th>",x["Last_price"],"</th>","<th>",x["category_id"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")
 '''To particular search'''
 if(b1=="PSearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['products']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Product id</th><th>Product name</th><th>Description</th><th>Standard Cost</th><th>Last Price</th><th>Category Id</th></tr>")
   for x in collection.find({'ord_id':t1}):
    print("<tr><th>",x["prod_id"],"</th>","<th>",x["prod_nm"],"</th>","<th>",x["description"],"</th>","<th>",x["standard_cost"],"</th>","<th>",x["Last_price"],"</th>","<th>",x["category_id"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")
 if(b1=="Update"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['products']
   collection.update_many({'prod_id':t1},{'$set':{'prod_nm':t2,'description':t3,'standard_cost':t4,'Last_price':t5,'category_id':t6}})
   print("<script>alert('Record Updated...')</script>")
except Exception:
        traceback.print_exc()
