import csv

class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # run validations for the received parameters to check errors
        assert price >= 0, "Price {} is not greater than or equal to zero!".format(price)
        assert quantity >= 0, "Quantity {} is not greater than or equal to zero!".format(quantity)

        # Assign self to object
        self.name = name
        self.price = price
        self.quantity = quantity

        # actions to execute anything an instance is instantiated to help keep track of all instances
        Item.all.append(self)

    def calculator_total_cost(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity"))

            )

    @staticmethod               # point zeros are also considered as integers
    def is_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False



    def __repr__(self):
        return "Item ('{}', {}, {})".format(self.name, self.price, self.quantity) # changing how it appears in the console


# Item.instantiate_from_csv()
# print(Item.all)

print(Item.is_integer(7))





