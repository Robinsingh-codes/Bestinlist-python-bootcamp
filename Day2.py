In [4]:
print('30 days 30 hour challenge')
print("30 days 30 hour challenge")
In [5]:
#Assigning String to Variable:
In [6]:
Hours= "thirty"
print(Hours)
In [7]:
#Indexing using String:
Days="Thirty Days"
print(Days[3])
In [11]:
# print the particular character from certain text (Slicing)
A="I will Code"
print(A[2:])
print(A[7:11])
# spaces contain indexing !!!
In [13]:
#Printing the Length of the character
a = "Im a Python Programmer"
print(len(a))
#Spaces also contain Length !!!
In [15]:
# Converting Lower Case and Upper Case character
b="Im A Python Programmer"
print(b.lower()) #Converting to all lower case
c="im a python Programmer"
print(c.upper()) #Converting to all Upper Case
In [16]:
#String Concatenation – Joining two strings
d="30 Days"
e="30 Hours"
f=d+e
print(f) # Note there is no space in between the words
In [18]:
# TO add spaces
d="30 Days"
e="30 Hours"
f=d+" "+e
print(f)
In [19]:
# Case Fold
text = "Thirty days and Thirty hours"
x = text.casefold()
print(x) # Converts All into lower case in Paragraph
In [21]:
text = "Thirty days and Thirty hours"
x = text.capitalize()
print(x)
In [27]:
text = "Thirty days and Thirty hours"
x = text.find("i")
print(x) # find how many letters are there
In [30]:
text = "Thirty days and Thirty hours"
x = text.isalpha()
print(x)
y="pythonProgrammer"
z=y.isalpha()
print(z)
# returns False if the string contians (space)!#%&?
In [33]:
txt = "Company10"
x = txt.isalnum()
print(x)
y="python Programmer"
z=y.isalnum()
print(z)
#returns False if the string contians (space)
#This method returns true if all characters in the string are alphanumeric and there is a
t least one character, false otherwise.
