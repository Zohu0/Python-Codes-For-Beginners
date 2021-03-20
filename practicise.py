class Programmer:
    company = "Microsoft"

    def detail(self, name, product):
        self.name=name
        self.product=product

    def getinfo(self):
        print(f"Name Of The Employee:{self.name}\n Product Of The Employee Is:{self.product}")

a= Programmer()
a.detail("Zohaib","Coding")
a.getinfo()
