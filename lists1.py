mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
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
mylist.sort()
print("Sorted list:", mylist)

#this will reverse the list
mylist.reverse()
print("Reversed list:", mylist)
mylist.extend([5, 6, 7])
print("Extended list:", mylist)
print("Index of 4:", mylist.index(4))
mylist.pop()
print("After pop:", mylist)
mylist.clear()
print("Cleared list:", mylist)
print("Is list empty?", len(mylist) == 0)



