#loop
'''str="hello"
for ch in str:
    print(str)
# range=>attribute
#printing odd no.

for i in range(1,10,2): #(start,end,diff)
    print(i)
#taking list and print the sum from these list
list =[10,20,30,40]
sum=0
for i in list:
    print(i)
    sum+=i
print("sum =",sum)'''
#printing number in descending number
for x in range(10,0, -1): #end,start,diff
    print(x)
#display the elements of a list
#it also storing the diff type of data
list=[10,10.3,'A','Pune']
for element in list:
    print(element)
#while_loop(we have to decalre first i and then while)
i=1
while i<=10:
    print(i)
    i=i+1 #increment operation
#nested loops
for i in range(3):
    for j in range(4):
        print("i=",i,'\t',"j=",j)

