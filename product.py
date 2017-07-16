class Product(object):
    def __init__(self, price, item_name, weight, brand, cost, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"


    def sell(self):
        self.status = "sold"
        self.price = self.price
        return self


    def addTax(self, x):
        tax = x
        self.price += self.price * x
        return self

    def exchange(self, x):
        reason_for_return = x
        if reason_for_return =="opened":
            self.status = "for sale 20% off"
            self.price -= self.price * .20
        elif "in the box, like new":
            self.status = "for sale"
            self.price = self.price
        elif reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
        return self

    def displayInfo(self):
        print ""
        print str(self.item_name)
        print "by " + str(self.brand)
        print "Only $" + str(self.price) + "!"
        print str(self.weight) + " lbs"
        print str(self.cost)
        print str(self.status)
        return self

product1 = Product(30, "Waffle-Iron", 5, "Sony", "cost effective", "for sale")
product1.displayInfo().addTax(0.09).displayInfo().sell().displayInfo()
product1.exchange("in the box, like new").displayInfo()

product2 = Product(499, "Goldfish-Cracker Fountain", 350, "Sharper Image", "not cost effective", "for sale")
product2.displayInfo().addTax(0.09).displayInfo().sell().displayInfo()
product2.exchange("opened").displayInfo().addTax(0.09).displayInfo().sell().displayInfo

product3 = Product(5, "Bubblewrap", 0.5, "Apple", "very cost effective", "for sale")
product3.displayInfo().addTax(0.09).displayInfo().sell().displayInfo()
product3.exchange("defective").displayInfo()
