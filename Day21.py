# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#mysql

def listOfTuples(l1, l2):
    return list(map(lambda x, y: (x, y), l1, l2))


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(listOfTuples(list1, list2))


def merge(list1, list2):
    merged_list = list(zip(list1, list2))
    return merged_list


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(merge(list1, list2))

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
result = tuple(zip(list1, list2))
print(result)

list1 = [23, 45, 54, 32, 78, 88, 22]
list2 = sorted(list1)
print(list2)


def filtereven(nums):
    if nums % 2 != 0:
        return True
    else:
        return False


numbers = [23, 11, 44, 34, 23, 25, 26, 27, 28, 34, 35, 36]
result = filter(filtereven, numbers)
for i in result:
    print(i)
