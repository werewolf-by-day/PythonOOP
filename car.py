class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

    def tax(self):
        if self.price > 10000:
            return 0.15
        else:
            return 0.12

    def display_all(self):
        print "Price: " + str(self.price)
        print "Speed: " + str(self.speed) + "mph"
        print "Fuel: " + str(self.fuel)
        print "Mileage: " + str(self.mileage) + "mpg"
        print "Tax: " + str(self.tax)

car1 = Car(2000, 50, "Full", 30,)
car1.display_all()
