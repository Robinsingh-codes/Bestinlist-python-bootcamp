 

#1
#1 # program to add +2 to every elemet of the list
lst_1 = [1,2,3,4,5,6,7,8,9]
l = []
n = len(lst_1)
for i in lst_1:
    l.append(i+2)
print(l)

#2

n = int(5)
for i in range(n):
    print(''.join(map(str,range(n-i,0,-1))))

#3
#fibonacci series program
n = int(5)
a = 0
b = 1
sum = 0
count = 1
print("fibonacci series:",end = "")
while(count <= n):
    print(sum,end ="")
    count += 1
    a = b
    b = sum
    sum = a + b
#print("\n")
#4
#amrstrong number program
num_25 = int(154)
sum_25 = 0
temp_1 = num_25
while temp_1>0:
    digit_25 = temp_1%10
    sum_25+=digit_25**3
    temp_1//=10
if num_25 == sum_25:
    print(num_25,"is amrstrong")
else:
    print(num_25,"is not amrstrong")

#5
#program of multiplication table of 9
n_156 = int(9)
mul_21 = 0
print("multiplication table of : 9",)
for p in range(1,10+1):
    mul_21 = n_156*p
    print(n_156 ,"x", p ,"=", mul_21 )

#6
# program to find the given number is
#print("\n")
n_ttt = int(50)
if n_ttt > 0:
    print("number is positive")
elif n_ttt<0:
    print("number is negative")
else:
    print("number is neither positive nor negative")

#7
#programm to convert days to ages

def find(ins_12345):
    year = int(ins_12345/365)
    week = int((ins_12345%365)/day_check)
    days = int((ins_12345%365)%day_check)

    print(year ,": years,",week,": weeks ,",days , ":days")

ins_12345 = int(402)
day_check = 7
find(ins_12345)

#8
#trignometry programm using math function

import math

a_b = math.pi/6
print("the value of sine of pi/6 is:",end="")
print(math.sin(a_b))
print("the value of cosine of pi/6 is:",end="")
print(math.cos(a_b))

#9
#basic calculator programm

print('calculator')
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

ch = int(input("enter choice(1-4):"))

if ch ==1:
    a =int(input("enter a:"))
    b = int(input("enter b:"))
    c = a+b
    print("sum=",c)
elif ch == 2:
    a = int(input("enter a:"))
    b = int(input("enter b:"))
    c = a - b
    print("difference = ",c)
elif ch==3:
    a = int(input("enter a:"))
    b = int(input("enter b:"))
    c = a * b
    print("product = ", c)
elif ch==4:
    a = int(input("enter a:"))
    b = int(input("enter b:"))
    c = a / b
    print("quotient = ", c)
