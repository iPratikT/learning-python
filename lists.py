#this will create an empty list and add elements to it
#there is an error in the code below, can you spot it?


mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append("hello")
print(mylist)

#this will remove the first occurrence of 2
mylist.remove(2)
print(mylist)

#this will insert 4 at index 1
mylist.insert(1, 4)
print(mylist)

#this will print the length of the list
print("Length of list:", len(mylist))

#this will sort the list
#this wont work if the list contains a string
mylist.sort()
print("Sorted list:", mylist)

#this will reverse the list
mylist.reverse()
print("Reversed list:", mylist)

#this will extend the list by adding multiple elements
mylist.extend([5, 6, 7])
print("Extended list:", mylist)

#this will count the occurrences of 4 in the list
print("Index of 4:", mylist.index(4))

#this will pop the last element from the list
mylist.pop()
print("After pop:", mylist)

#this will clear the list
mylist.clear()
print("Cleared list:", mylist)
print("Is list empty?", len(mylist) == 0)