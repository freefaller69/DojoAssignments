class Animal(object):
    def __init__(self, name):
        print "New animal created"
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print self.name, self.health
        return self.name, self.health

a = Animal('cat')

a.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        print "Dog Created"
        self.health = 150

    def pet(self):
        self.health += 5
        return self

beagle = Dog("Snoopy")

beagle.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        print "Dragon Created"
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        print "This is a dragon!"
        super(Dragon, self).displayHealth()


d = Dragon("Smaug")
d.walk().walk().walk().run().run().fly().fly().displayHealth()
