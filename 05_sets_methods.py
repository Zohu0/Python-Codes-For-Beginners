# Creating An Empty Set

b= set()
print(type(b))

# Adding element to set
b.add(4)
b.add(6)
b.add(5)
b.add(6)
b.add((3,4,5)) # We can add tuple to set but not list
print(b)

print(len(b)) # print the length of the set

b.remove(6)
print(b)

