from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    description: str
    quantity: int

    def check_quantity(self, quantity) -> bool:
        if self.quantity >= quantity:
            return True

        return False

    def buy(self, quantity):
        if self.quantity < quantity:
            raise ValueError

        self.quantity -= quantity

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    products: dict[Product, int]

    def __init__(self):
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count

    def remove_product(self, product: Product, remove_count=None):
        if product not in self.products:
            return

        if remove_count is None:
            del self.products[product]
        elif remove_count >= self.products[product]:
            del self.products[product]
        else:
            self.products[product] -= remove_count

    def clear(self):
        self.products = {}

    def get_total_price(self) -> float:
        total = 0
        for product in self.products:
            total += product.price * self.products[product]
        return total

    def buy(self):
        for product, quantity in self.products.items():
            product.buy(quantity)
        self.clear()
