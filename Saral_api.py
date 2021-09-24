
import requests
import json 
from pprint import pprint
a = requests.get("http://saral.navgurukul.org/api/courses")
xx = a.json()
s = json.dumps(xx, indent=4)
with open("courses.json","w") as file:
    file.write(s)
file=open("courses.json","r")
b=json.load(file)
c=[]
d=1
for i in b["availableCourses"]:
    print(d,i["name"],i['id'])
    c.append(i["id"])
    d+=1
use = int(input("Enter the number :"))
user=c[use-1]
e = requests.get("http://saral.navgurukul.org/api/courses/"+str(user)+"/exercises")
ee = e.json()
with open("courses1.json","w+") as f:
    j=json.dump(ee,f,indent=4)
j = open("courses1.json", "r")
m = json.load(j)
v = 1
a={}
slug_list=[]
for l in m["data"]:
    print(v,":",l['name'])
    slug_list.append(l["slug"])
    a[v]=l["slug"]
    x = 1
    for i in l['childExercises']:
        z = str(v)+"."+str(x) 
        print("   ",z,i["name"])
        a[z]=i["slug"]
        x+=1     
    v+=1
user1 = (input("Please write the number :"))
for i in a:
    if user1==str(i):
        print(a[i])
        res = requests.get("http://saral.navgurukul.org/api/courses/12/exercise/getBySlug?slug="+a[i])
        rest=res.json()
        with open("courses2.json", "w+") as o:
            ll=json.dump(rest,o,indent=4)
        ll=open("courses2.json", "r")
        n=json.load(ll)
        print(n["content"])