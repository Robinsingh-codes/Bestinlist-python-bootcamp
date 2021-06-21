#1
a= { "caption":"kholi","vice caption":"rahane","wicket keeper":"rishab pant"}
b = { "bowler":"shami","spiner":"ashwin"}
a.update(b)
print(a)
#2
p = [9,8,7,6,5,4,4]
p.sort()
set1 = set(p)
print(set1)
#3
month ={ "one":"monday","two":"tuesday","three":"wednesday"}
print(month)
print(len(month.keys()))
print(sorted(month.items()),end="")
for i in sorted(month.keys()):
    print(i)
#4
string = input("enter your second name:",)
string2 = input("enter your first name:")
string3 = string.replace(string[0],string2)
print(string3)
#5
new = input("enter your name:")
r = new.capitalize()
print(r)
#6
a =[1,1,2,2,3,4,3,2,1,3]
b =[]
   for  i in a:
     if a.count(i)>1:
         if i not in b:
             b.append(i)
print(b)
#7
a=int(input("Enter number :"))
b=int(input("Enter number :"))
c=int(input("Enter number :"))
sum1=a+b+c
print(sum1)
user=int(input("Enter the number to divide sum!"))
if sum1% user==0:
print("The given input divide the sum",user)
else :
print("The given input does not divide sum",user)
#8
n=[1,2,3,1,2,3,4,5,5,5]
import statistics
print(statistics.mean(n))
print(statistics.median(n))
print(statistics.mode(n))
#9
a=input("enter the text1 ")
b=input("entern the text2 ")
print(a," ",b)
a,b=b,a
print("reversed element of a is ",a)
print("reversed element of b is ",b)
print(a,b)
#10
a1=33
print("Binary Value : ",bin(a1))
print("Octa Value : ",oct(a1)
