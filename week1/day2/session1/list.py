a = [1,2,3,56,78,47]

print(type(a))
# print
print(a)
# Look at a single element
print(a[-3])
# add new items
a.append(99)
print(a)
#add in the middle
a.insert(4,100)
print(a)
# remove items from value
a.remove(100)
print(a)
#remove using index
a.pop(1)
print(a)
# replace items
a[3] = 200
print(a)
#len of list
print(len(a))

a = [1,2,3]+[100,101,102]
print(a)

a.insert(len(a)//2,500)
print(a)

a = [1,2,4,5.6,99.12,"list 1","list 2"]
print(a)


a = [1,2,3,4,5,3]
a.remove(3)
print(a)

a = [56.8,[1,2,3],[4,5,6]]
print(a)

print(type(a[0]))