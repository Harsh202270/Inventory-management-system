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
t7=f.getvalue("t7")
t8=f.getvalue("t8")
b1=f.getvalue("b1")
try:
 if(b1=="Save"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['employees']
   insert1={'employee_id':t1,'first_nm':t2,'last_nm':t3,'email':t4,'phone':t5,'hire_date':t6,'manager_id':t7,'job_title':t8}
   collection.insert_one(insert1)
   print("<script>alert('Record Saved...')</script>")
   a=0
   for x in collection.find({}):
    if(t1==x['employee_id']):
     a=1
     break
   if(a==1): 
    print("<script>alert('Employee Id already exist')</script>")
   else:
    insert1={'employee_id':t1,'first_nm':t2,'last_nm':t3,'email':t4,'phone':t5,'hire_date':t6,'manager_id':t7,'job_title':t8}
    collection.insert_one(insert1)
    print("<script>alert('Record Saved...')</script>")
    print("<script>window.open('Employees.html','_self')</script>")
 if(b1=="Delete"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['employees']
   delete1={'employee_id':t1}
   collection.delete_many(delete1)
   print("<script>alert('Record Deleted...')</script>")
   print("<script>window.open('Employees.html','_self')</script>")
 '''To All Search'''
 if(b1=="All Search"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['employees']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Employee id</th><th>First name</th><th>Last name</th><th>Email Id</th><th>Phone no.</th><th>Hire Date</th><th>Manager Id</th><th>Job Title</th></tr>")
   for x in collection.find({}):
    print("<tr><th>",x["employee_id"],"</th>","<th>",x["first_nm"],"</th>","<th>",x["last_nm"],"</th>","<th>",x["email"],"</th>","<th>",x["phone"],"</th>","<th>",x["hire_date"],"</th>","<th>",x["manager_id"],"</th>","<th>",x["job_title"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")
 '''To particular search'''
 if(b1=="PSearch"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['employees']
   print("<body bgcolor=pink><table border=2 bgcolor=grey><tr><th>Employee id</th><th>First name</th><th>Last name</th><th>Email Id</th><th>Phone no.</th><th>Hire Date</th><th>Manager Id</th><th>Job Title</th></tr>")
   for x in collection.find({'employee_id':t1}):
    print("<tr><th>",x["employee_id"],"</th>","<th>",x["first_nm"],"</th>","<th>",x["last_nm"],"</th>","<th>",x["email"],"</th>","<th>",x["phone"],"</th>","<th>",x["hire_date"],"</th>","<th>",x["manager_id"],"</th>","<th>",x["job_title"],"</th></tr>")
   print("<body><input type=button value='Print' onclick=window.print()></body>")
 if(b1=="Update"):
   client=pymongo.MongoClient("mongodb://localhost:27017/")
   db=client['inventory']
   collection=db['employees']
   collection.update_many({'employee_id':t1},{'$set':{'first_nm':t2,'last_nm':t3,'email':t4,'phone':t5,'hire_date':t6,'manager_id':t7,'job_title':t8}})
   print("<script>alert('Record Updated...')</script>")
except Exception:
        traceback.print_exc()
