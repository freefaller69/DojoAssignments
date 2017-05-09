class Product(object):
    def __init__(self, price, item_name, weight, brand, cost, status="For Sale"):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status
    def sell(self):
        self.status = "Sold"
        return self
    def tax(self, taxRate):
        self.tax = self.price * taxRate
        return self
    def product_return(self, reason):
        self.reason = reason
        if self.reason == "defective":
            self.status = self.reason
            self.price = 0
        elif self.reason == "opened":
            self.status = "used"
            self.price = self.price * 0.8
        else:
            self.status = "for sale"
        return self
    def display_info(self):
        print "Price:",self.price
        print "Tax:",self.tax
        print "Total Price:",self.price + self.tax
        print "Item:",self.item_name
        print "Weight:",self.weight
        print "Brand:",self.brand
        print "Cost:",self.cost
        print "Status:",self.status

product1 = Product(299.00, "Xbox", "5 lb", "Microsoft", 250.00)

# product1.sell().tax(0.08).display_info()
product1.product_return("defective").tax(0.08).display_info()
