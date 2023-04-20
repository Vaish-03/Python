#datatype
#print the data type of varible
x = 5
print(type(x)) #clas 'int'>
y = -4
print(type(y)) #minus value consider in int

num = 2.0
print(type(num)) #<class 'float'>

num1 =8 + 9j
print(type(num1))#<class 'complex'>
 #a  ->nameerror(it is mandatory to write none)
# print(a)
#a = none
#print(a)

str = "Hello"
print(type(str))

emp = ["name",'id',"salary"]  #list
print(type(emp))
print(emp)

Marks = ("HSCmarks","graduaction")  #tuple
print(type(Marks))
print(Marks)

stud = {"Name":"Vaishnavi","Div":"C"}
print(stud)
print(type(stud))
#type conversion
a = 5.6
b=int(a)
print(b) #convertint 5.6 into 5(float to int)
print(type(b))

p=7
q=complex(p,b)
print(q)
print(type(q))

bool = p>b
print(bool)
print(type(bool))

c =int(True) #1
print(c)

e =float(True) #1.0
print(e)

d =float(False) #0.0
print(d)

z = range(10) #range bet 0 to 10
print(z)
print(type(z))

o = list(range(10))#print the 0-9 num
print(o)

s = list(range(4,10,2)) #4->start,10->end,2->diff
print(s)
print(type(s))
#dictionary
t ={'rollno':'31','name':'vaishnavi','sub':'cloud'}
print(t.keys())
print(t.values())
print(t['sub'])
