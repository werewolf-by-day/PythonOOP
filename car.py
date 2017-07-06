class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12


    def display_all(self):
        print " "
        print "Price: " + str(self.price)
        print "Speed: " + str(self.speed) + "mph"
        print "Fuel: " + str(self.fuel)
        print "Mileage: " + str(self.mileage) + "mpg"
        print "Tax: " + str(self.tax)

car1 = Car(2000, 50, "Full", 30)
car1.display_all()

car2 = Car(15000, 60, "Kind of Full", 35)
car2.display_all()

car3 = Car(1000, 10, "Empty", 60)
car3.display_all()

car4 = Car(25000, 90, "Kind of Full", 25)
car4.display_all()

car5 = Car(10000, 25, "Full", 50)
car5.display_all()

car6 = Car(10001, 55, "Empty", 40)
car6.display_all()
