class Employee:
    company= "Google" # Class Attribute  Remains For Every Object Of Class

zohaib=Employee()
yusuf=Employee()
satyam=Employee()
salman=Employee()
print("Zohaib Is Employee Of:",zohaib.company)
print("Yusuf Is Employee Of:",yusuf.company)
Employee.company= "Youtube" # You Can Change Class Attribute Of Object BY This Method
print("Satyam is Employee Of:",satyam.company)
print("Salman Is Employee Of:", salman.company)
print("Zohaib Is Employee Of:",zohaib.company)