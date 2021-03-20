class Employee:
    company= "Google"

zohaib=Employee()
yusuf=Employee()
satyam=Employee()
salman=Employee()
zohaib.salary= 40000 #Instance Attribute For Zohaib Salary
yusuf.salary= 60000 # Instance Attribute For Yusuf Salary
satyam.salary= 160000 # Instance Attribute For Satyam Salary
salman.salary= 120000 # Instance Attribute for Salman Salary
print("Zohaib Is Employee Of:",zohaib.company)
print("Yusuf Is Employee Of:",yusuf.company)
Employee.company= "Youtube"
print("Satyam is Employee Of:",satyam.company)
print("Salman Is Employee Of:", salman.company)

print("Zohaib Salary:", zohaib.salary)
print("Yusuf Salary:", yusuf.salary)
print("Satyam Salary:",satyam.salary)
print("Salman Salary:",salman.salary)