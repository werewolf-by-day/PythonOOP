class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print "This bike is $" + str(self.price)
        print "The max speed of this bike is " + str(self.max_speed) + "mph"
        print "Total miles: " + str(self.miles) + " miles"

    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing"
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
        return self

bike1 = Bike(100, 30, 400)
bike1.ride().ride().ride().reverse().displayInfo()

bike2 = Bike(250, 35, 0)
bike2.ride().ride().reverse().reverse().displayInfo()

bike3 = Bike(679, 42, 20)
bike3.reverse().reverse().reverse().displayInfo()
