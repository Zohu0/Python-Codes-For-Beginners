class Railway:
    def __init__(self, name,seat,fare):
        self.name=name
        self.seat=seat
        self.fare=fare

    def getinfo(self):
        print(f"The Name Of The Train Is :{self.name}")
        print(f"The Seat Available Is    :{self.seat}")
        print(f"The Fare Of The Train Is :{self.fare}")

    def bookticket(self):
        if (self.seat>0):
            print(f"Your Ticket Has Been Book! Your Seat No Is: {self.seat}")
            self.seat=self.seat-1
        else:
            print("Sorry No Ticket Available")

    

a= Railway("Kafiyat Express", 10, 1850)
a.getinfo()
a.bookticket()
a.getinfo()