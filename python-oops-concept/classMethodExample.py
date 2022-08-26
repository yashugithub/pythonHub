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

  #  def __repr__(self):
   #     return f'Bike("{self.description}", {self.condition}, {self.sale_price}, {self.cost})'

    @classmethod
    def get_default_bike(cls):
        return cls('Bike test', Condition.OKAY, sale_price=100, cost=10)


# Create Tricycle object and inherit the BikeObject
class Tricycle(BikeObj):
    pass


if __name__ == '__main__':
    bike1 = BikeObj.get_default_bike()
    print(repr(bike1))

    # test get_default_bike in Tricycle
    triBike = Tricycle.get_default_bike()
    print(triBike)
