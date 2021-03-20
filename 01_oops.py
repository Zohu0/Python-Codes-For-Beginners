class RailwayForm:
    formtype= "Railway form"
    def printdata(self):
        print(f"Name Is {self.name}")
        print(f"Train Is {self.train}")
        print(f"Seat Is {self.seat}")

zohaibapplication=RailwayForm()
zohaibapplication.name= "Zohaib"
zohaibapplication.train= "Rajdhani Express"
zohaibapplication.seat= "A1 52"
zohaibapplication.printdata()