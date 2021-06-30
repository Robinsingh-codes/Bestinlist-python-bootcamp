#list down Error
#Name error
list = 12
print(list1)

#2
#TYpeError
a = '123'
a+= 123
#3
#TypeError
l = [1,2,3,4,5,6]
for i in range(2,1):
    print(i+1)

#4
#syntax Error
for i range(1,10):
    print(i)
#5
#index error
l = [1,2,3.4,5,56,7]
for i in range(len(l)):
    print(l[i+1])
#6

#module not fount error
import modulexyz
#7
#design a simple calculator using try and except
def calculate():
    try:
        print('+')
        print('-')
        print('*')
        print('/')
        print('%')
        print('**')
        operation = input("Select an operator:n")
        print("Enter two numbers")
        number_1 = int(input())
        number_2 = int(input())
        if operation == '+': # To add two numbers
            print(number_1 + number_2)
        elif operation == '-': # To subtract two numbers
            print(number_1 - number_2)
        elif operation == '*': # To multiply two numbers
            print(number_1 * number_2)
        elif operation == '/': # To divide two numbers
            print(number_1 / number_2)
        elif operation == '%': # To remainder two numbers
            print(number_1 % number_2)
        elif operation == '**': # To num1 exponent num2
            print(number_1 ** number_2)
        else:
            print('Invalid Input')
    except Exception as e:
        print(e)

#8 
#print one message if try block raises a nameError and another for other error
try:
    a = 123
    if a==123:
        print(b)
        raise NameError("Name error")
    if a >0:
        raise ValueError("Value error")
except NameError as ne:
        print(ne)
except ValueError as ve:
    pritn(ve)

#9 
#when try - except scenario is not required?
#python Exception are error scenarios that alter the normal execution flow of the program the process of the code inside the elseblock is executed if there are no exception raised

#10 
#try getting an input inside try catch block
try:
    age=int(input('Enter your age: '))
except:
    print ('You have entered an invalid value.')
