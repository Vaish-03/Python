#If Statement
'''`if True:
    print("in right")
print("bye")'''
#even or odd
#if...else
x=int(input("Enter num:")) #taking in from user
if x%2==0:
    print(x,"is even")
else:
    print(x,"is odd")
#if else if(Nested)
if x%2==0:
    print(x,"is even")
    if(x>=6):
        print(x,"is greater than 6")
    if(x>=10):
        print(x,"is greater than 10")
else:
    print(x,"is odd num")
#elif
#if-elif-else
a=int(input("Enter no.:"))
if a==1:
    print("One")
elif a==2:
    print("two")
elif a==3:
    print("three")
elif a==4:
    print("four")
elif a==5:
    print("five")
else:
    print("wrong input")
