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
try:
 if(b1=="Save"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['product_categories']
   a=0
   for x in collection.find({}):
    if(t1==x['category_id']):
     a=1
     break
   if(a==1): 
    print("<script>alert('Category Id already exist')</script>")
   else:
    insert1={'category_id':t1,'category_nm':t2}
    collection.insert_one(insert1)
    print("<script>alert('Record Saved...')</script>")
    print("<script>window.open('Product_Category.html','_self')</script>")
 if(b1=="Delete"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['product_categories']
   delete1={'category_id':t1}
   collection.delete_many(delete1)
   print("<script>alert('Record Deleted...')</script>")
   print("<script>window.open('Product_Category.html','_self')</script>")
 '''To All Search'''
 if(b1=="All Search"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['product_categories']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Category Id</th><th>Category Name</th></tr>")
   for x in collection.find({}):
    print("<tr><th>",x["category_id"],"</th>","<th>",x["category_nm"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")
 '''To particular search'''
 if(b1=="PSearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['product_categories']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Category Id</th><th>Category Name</th></tr>")
   for x in collection.find({'category_id':t1}):
    print("<tr><th>",x["category_id"],"</th>","<th>",x["category_nm"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")
 if(b1=="Update"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['product_categories']
   collection.update_many({'category_id':t1},{'$set':{'category_nm':t2}})
   print("<script>alert('Record Updated...')</script>")
except Exception:
        traceback.print_exc()
