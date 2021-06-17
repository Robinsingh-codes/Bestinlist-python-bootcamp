#python script to merge two dictionaries
def Merge(dict1 , dict2):
    s = {**dict1 ,** dict2}
    return s

dict1 = {"maharashtra":"pune","goa":"panji","madhya pradesh":"bhopal","karnataka":"banglore","up":"bihar"}
dict2 = {"japan":"tokyo","china":"shanghai","nepal":"kathmandu","australia":"sydney","pakistan":"lahore"}
dict3 = Merge(dict1 , dict2)
print(dict3)


#removing a key from dictionaries
dict7={"maharashtra":"pune","goa":"panji","madhya pradesh":"bhopal"}
dict7.pop("maharashtra")
print(dict7)


# program to map two list into dictionary
lst1 = []
kil = []
n = int (input("enter the number of elements for dictionaries:"))
print("For keys:")
for x in range(0,n):
    element = input("enter element" + str(x+1) + ":")
    lst1.append(element)
print("For values:")
for x in range(0,n):
    element = input("enter element" + str(x + 1) + ":")
    kil.append(element)
d = dict(zip(lst1,kil))
print("the dictionary is:")
print(d)


#program to find length of set
dict4 = {"shkjs":5,"wuyiui":6,"ajshuw":8,"powsms":9}
print("length of set:",len(dict4))


#removing intersection of 2nd set from 1st set:
print("removing intersection of 2nd set from 1st set:")
s1 = {1,2,3,4,5}
s2 = {2,3,8,6,4}
print("original set:")
print(s1,"\n",s2)

s1.difference_update(s2)
print("set 1 : " , s1)
print("set 2 :", s2)
