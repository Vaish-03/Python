#INPUT AND OUTPUT
#both are same
print("Hello")
print('hello')

# /t=>tab space and \n=>new line
print("this is \nnew line")
print("this is \t new line")
#repetition of string(*)
print(4 *'zeal')
#concate(joining)
print('city = '+'pune')
print("city =","pune")
#sep attributes
a,b=2,4
print(a,b)
print(a, b, sep=',')
print(a, b, sep=':')
print(a, b, sep='----')
#3 print on single line
print("hello",end='')
print("Dear",end='')
print("How are u?")

#take the user input
x=input("ENter string:")
print(x)   #print the string

y=int(input("Enter the no: "))
print(y)  #print the int

z=float(input("Enter the float value: "))
print(z)   #print the float
#multiple inputs on same line(accpect 3 int on same line)
var1, var2, var3 = [int(x) for x in input("Enter three number: ").split(',')]
print('sum=',var1+var2+var3)