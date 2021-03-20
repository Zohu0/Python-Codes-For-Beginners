class Employee:
    company= "GOOGLE"


    def __init__(self, name, salary, company):
        print("Employee Is Created:")
        self.name=name
        self.salary=salary
        self.company=company

    def getdetails(self):
        print("The Name Of The Employee Is:", self.name)
        print("The Salary Of The Employee Is:",self.salary)
        print("The Company Of The Employee Is:",self.company)



zohaib=Employee("Zohaib", "100k", "Google")
zohaib.getdetails()


