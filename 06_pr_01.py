myDict= {"kutta": "Dog",
"billi": "Cat",
"haathi": "Elephant"}

print("Your Options Are", myDict.keys())

a= input("Enter Your Hindi Word: ")
# print("The Meaning Of Your Word: ", myDict[a])
print("The Meaning Of Your Word: ", myDict.get(a))

