
from enum import Enum

class Condition(Enum):
    NEW = 0
    OKAY = 1
    GOOD = 2
    BAD = 3

class MethodNotAllowed(Exception):
    pass


class Bike:

    def __init__(self, description, condition, sale_price, cost=0):
        print("__init__ called")
        self.description = description
        self.condition = condition
        self.sale_price = sale_price
        self.cost = cost

        self.sold = False

    def service(self, cost=0, new_condition=None, new_sale_price=None):
        self.cost += cost
        if new_condition:
            self.condition = new_condition
        if new_sale_price:
            self.sale_price = new_sale_price

    def update_sale_price(self, new_sale_price):
        if self.sold:
            raise MethodNotAllowed("Can not update new sale price for a sold bike")
        self.sale_price = new_sale_price

    def sell(self):
        if self.sold:
            raise MethodNotAllowed("Can not sale, this bike is already sold")
        self.sold = True
        profit = self.sale_price - self.cost
        return profit

if __name__ == '__main__':
    bike1 = Bike('Red Bike', Condition.GOOD, sale_price=400, cost=50)
    bike1.service(15, new_sale_price=350)  # we can also call like Bike.service(bike1)
    print("sale price after service:: "+str(bike1.sale_price))
    bike1.update_sale_price(new_sale_price=500)
    print("sale price after updating:: "+str(bike1.sale_price))
    profit = bike1.sell()
    print('sell profit :: ' + str(profit))

    # print the error
    bike1.update_sale_price(new_sale_price=500)


    print(vars(bike1))

    print("\n\n")

    print(vars(Bike))
