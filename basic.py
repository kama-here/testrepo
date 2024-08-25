import math
print("siuuuu")
print(math.gcd(5,15))
name1= "kama"
name2 ="shreyuu"
temp="{} find his home in {}".format(name1,name2)
temp= f"{name1} finds his home in {name2}"
print(temp)
t= ("shreyu","puchku","bunny")
t= list(t)
var= type(t)
t.insert(1,"raju")
t.pop()
print(var)
print(t)
t.append("raju")
s= {2,2,2,9,0,9,0,7,5,5,3,33,3,3,333,8,9,0}
s.add(23)
#s.update([2,3,4,5,6,7,7,89,9])
s.remove(23)
print(s)
age=input("enter age")
v= type(age)
print(v)
age = int(age)
if(age>18):
    print("drive")
elif(age<0):
    print("please let him born")
else:
    print("tohar mai ke chudo")
t=set(t)
print (t)
def nomnom(a,b):
    a=a*b
    b=b*b
    print(b)
    return a
print(nomnom(4,5))

class employee:
    def __init__(self,name,salary):  #constructor
        self.name=name
        self.salary=salary
siuuu= employee("kama",2000)         #parameterized
print(siuuu.name)
print(siuuu.salary)
    