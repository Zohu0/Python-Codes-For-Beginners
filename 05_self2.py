class Employee:
    company= "GOOGLE"
    def get_salary(self):
        print(f"Salary for {self.name} working in {self.company} is {self.salary}")

zohaib= Employee()
zohaib.salary=100000
zohaib.name="Zohaib"
zohaib.get_salary() # Employee.get_salary(zohaib)


