l1 = [3, 432, 234, 12, 1, 22, "piyush"]

print("type of l1 is: " , type(l1))
print(l1)

l1.pop()
print("l1 after pop  is:" , l1)

l1.remove(432)
print("li after removing 432 is: " , l1)

l1.sort()
print("l1 after sorting is: " , l1)

l1.extend([21, 55, 323])
print("l1 after adding new value is: " , l1)