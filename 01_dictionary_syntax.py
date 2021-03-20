myDict= {
    "Fast": "In A Quick Manner",
    "Lion": "A King Of Jungle",
    "Marks": [1,2,3,4],
    "Anotherdict": {"Zohaib": "A Name"} # Work As Nested Dictionary
}

print(myDict["Fast"])
print(myDict["Lion"])
print(myDict["Marks"])
myDict["Marks"]= [23,56,78,45]
print(myDict["Marks"]) # Change The Dictionary Element
print(myDict["Anotherdict"]["Zohaib"]) # Print "A Name"