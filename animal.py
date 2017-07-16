class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
        if self.health > 0:
            self.heath = 0

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print str(self.name) + "'s current health is " + str(self.health)
        if self.health < 1:
            print str(self.name) + " has fainted!"

animal1 = Animal("Cat")
animal1.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self


Dog = Dog("Fido")
Dog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        print "I am a Dragon"
        super(Dragon, self).displayHealth()

dragon1 = Dragon("Rhaegal")
dragon1.walk().run().fly().displayHealth()

animal2 = Animal("Komodo Dragon")
animal2.run().run().run().run().run().run().run().run().displayHealth()
