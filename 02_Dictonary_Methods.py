myDict= {
    "Fast": "In A Quick Manner",
    "Lion": "A King Of Jungle",
    "Marks": [1,2,3,4],
    "Anotherdict": {"Zohaib": "A Name"}, # Work As Nested Dictionary 
    1: 2
}

# Dictionary Methods
print(myDict.keys()) # Print the keys of dictionary
print(myDict.values()) # Print the value of dictionary
print(myDict.items()) # Print the (key and value) for all the content of dictionary

# print(myDict)
updatedict= {"Yusuf": "Friend"
}
myDict.update(updatedict) # To update in dictionary
print(myDict)

print(myDict.get("Lions")) # Return NONE if lions is not present in dictionaary
print(myDict["Lions"]) # Return Error If Lions Is not present in dictionary
