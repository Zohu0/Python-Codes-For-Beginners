letter= '''Dear <Name>,
You Are Selected!
Date: <Date>'''

name= input("Enter Your Name\n")
date= input("Enter Date\n")
letter.replace("<Name>", name)
letter.replace("<Date>", date)
print(letter)
