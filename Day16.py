#create lamda function that multiplies argument x with argument y
def myfunc(y):
    return lambda x:x*y
mydoubler = myfunc(3)
print(mydoubler(5))

#2

# python program to create fibonacci series using lambda
from functools import reduce
fib = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],range(n - 2), [0, 1])
print(fib(11))

#3

#program that multiply each noof givenlist with given nunber
nums = [2, 4, 6, 9 , 11]
n = 2
print("Original list: ", nums)
print("Given number: ", n)
filtered_numbers=list(map(lambda number:number*n,nums))
print("Result:")
print(' '.join(map(str,filtered_numbers)))

#4

#write a program to find number divisible by 9 from a list of number
list1=[2,4,5,6,7,8,9,21,12,14,15,27,36,81]
print(list1)
list2=list(map(lambda j:j%9==0,list1))
print("Result")
print(' '.join(map(str,list2)))
list2=list(filter(lambda j:j%9==0,list1))
print("Result")
print(' '.join(map(str,list2)))

#5


#program to count even no.
list1=[2,4,5,6,7,8,9,21,12,14,15,27,36,81]
print(list1)
list2=list(filter(lambda j:j%2==0,list1))
print("Result :")
print(len(list2))
