def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


#user input
a=int(input("Enter Firs Number"))
b=int(input("Enter Second Number"))
sum=a+b
print(sum)

#pyhton list
L1 = [12,14,16,18]
L2 = ["B","h","a","v","i"]
print(L1)
print(L2)

#python accesing list

L1=['B','h','a','v','a','n','i']
print(L1)
print(L1[5])   #L[5] returns the item at index 5
print(L1[1:])  #L[1:] returns objects from 1 to the last object
print(L1[1:3]) #L[1:3] returns a new list, containing the objects between 1 and 3.
print(L1[-1])  #L1 access the last item in the list
print(L1[-4:-1]) #L[-4:-1] returns a new list, containing the objects between -4 and -1.
print(L1[-5:])   #L[-5:] returns objects from -5 to the last object

L=['I','N','D','I','A','N']
L.append('S')               # Append add the value after the last item
print(L)


L=['I','N','D','I','A','N']
L.extend('WELCOME')        #Extends adds sequence or lists
print(L)

L=['I','N','D','I','A','N']
L.insert(7,'1')          #Inserts an item at a given index and move remaining items to right
print(L)

L=['I','N','D','I','A','N']
del L[5]                #Deletes the 5th Index item
print(L)

L=['I','N','D','I','A','N']
del L[5:6]             #Deletes items between 5 to 6
print(L)
del L[3:6]             #Deletes items between 3 to 6
print(L)

L=['I','N','D','I','A','N']
L.pop()               #Pops the last item
L.pop(4)              #pops the 4th index item in the list
L.remove('D')         #removes the item D from the list
print(L)
L=[100,50,110,250,350]
print(min(L))
print(max(L))
print(sorted(L))
L.sort()
print(L)

# Nested List
L=[1,2,["hello"],('hi')]
print(L)

T=(27,"Bhavi",'B',8.6) #Tuple with mixed datatypes
print(T)
print(T[2])             #Accessing tuple elements using indexing
print(T[1:])


#Exercise 1
# Write a program to create a list of n integer
L =[200,202,204,206,208,]
print(L)


# Add an item in to the list (using function)
L.append(202)
L.insert(0,202)
print(L)


# Delete (using function)
del L[0]
L.remove(204)
print(L)

#Store the largest number from the list to a variable
largvar=max(L)
print("The largest number from the list is :",largvar)
#Store the Smallest number from the list to a variable
smallvar= min(L)
print("The smallest number from the list is :",smallvar)

#Create a tuple and print the reverse of the created tuple
my_tuple=(6,5,4,3,2,1-1)
print(my_tuple[::-1])

my_tuple=('b','h','a','v','a','n')
print(my_tuple)
x = reversed(my_tuple)
print(tuple(x))

#Create a tuple and convert tuple into list

my_tuple=('b','h','a','v','a','n')
print(my_tuple)
print(list(my_tuple))
