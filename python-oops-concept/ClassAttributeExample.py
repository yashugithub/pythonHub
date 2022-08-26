
from enum import Enum

class Condition(Enum):
    NEW = 0
    OKAY = 1
    GOOD = 2
    BAD = 3

class MethodNotAllowed(Exception):
    pass


class BikeObj:

    # Define class attributes here
    num_wheels = 2

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
        
    @property
    def profit(self):
        if not self.sold:
            return None
        return self.sale_price - self.cost


if __name__ == '__main__':
    bike1 = BikeObj('Red Bike', Condition.GOOD, sale_price=400, cost=50)

    print(bike1.num_wheels)
    print(BikeObj.num_wheels)

    bike1.num_wheels = 10

    print(bike1.num_wheels)

    BikeObj.num_wheels = 3

    print(bike1.num_wheels)

    bike1.sell()
    # property test
    print(bike1.profit) # it print like <function BikeObj.profit at 0x0000026351941480> before adding @property annotation







