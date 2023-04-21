#Operators
#1)Arithmetic operators
print(13+5) #Addition
print(13-4) #sub
print(1*4) #Multipication
print(4/3) #division
print(4**2) #exponent
print(4%3) #module
print(4//3) #floor division

''' order of evaluation
1) paranthesis()
2)exponent
3)mul,div,module,floor division
4)add sub
'''
d = (1+2)**3*2//2+3
print(d)

#Assignment Operator
x=5
x += 3
print(x)
y=9
y -= 5
print(y)
z=4
z*=2
print(z)
a=4
a /=2
print(2)
b=3
b %=2
print(b)
c=4
c **=2
print(c)
d=5
d //=3
print(d)

#relational operator
x = 5
y = 3
print(x == y)

x = 5
y = 3
print(x != y)

x = 5
y = 3
print(x > y)

x = 5
y = 3
print(x < y)

x = 5
y = 3
print(x >= y)

x = 5
y = 3
print(x <= y)

#Logical operator
x = 5
print(x > 3 and x < 10) #and

x = 5
print(x > 3 or x < 10) #or

x = 5
print(not(x > 3 and x < 10))
a=2
b=3
print(a and b)#display 2 nd no. bcz it check both th conditions
print(a or b)#displays the 1 st no.

#identity operator=>is ,is not
m=3
n=4
print(m is n)
print(m is not n)

#Bitwise operator
#and operator
p=5
q=6
print(p&q)
s=12
t=6
print(s&t)
#or operator
p=5
q=6
print(p^q)
s=12
t=6
print(s^t)

#Bitwise operator
x=160
print(x<<3)#left shift
y=120
print(x>>2)




