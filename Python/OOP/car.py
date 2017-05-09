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
        print "Price:",self.price
        print "Speed:",self.speed
        print "Fuel:",self.fuel
        print "Mileage:",self.mileage
        print "Tax:",self.tax
car1 = Car(30000, "85mph", "full", "25mpg")
car2 = Car(100000, "210mph", "full", "15mpg")
car3 = Car(4000, "35mph", "not full", "35mpg")
car4 = Car(7000, "55mph", "empty", "27mpg")
car5 = Car(45000, "90mph", "full", "23mpg")
car6 = Car(2000, "150mph", "full", "5mpg")

car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()
