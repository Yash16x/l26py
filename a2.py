class Computer:
    def __init__(self):
        self.__maxprice = 90000

    def sell(self):
        print("Selling Price: {}".format(self .__maxprice))

    def setMaxPrice(self, price):
        self. maxprice = price

c = Computer()
c.sell()


c .__maxprice = 50000
c.sell()


c.setMaxPrice(1000)
c.sell()