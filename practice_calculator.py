class Calculator:
    def __init__(self, num):
        self.num=num

    def square(self):
        print(f"The Value of {self.num} Square is {self.num**2}")

    def squareroot(self):
        print(f"The Value of {self.num} Squareroot is {self.num**0.5}")

    def cube(self):
        print(f"The Value of {self.num} Cube is {self.num**3}")
        

a= Calculator(4)
a.square()
a.squareroot()
a.cube()