from .checkout import Checkout
from .shop import Shop

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    shop = Shop()
    shop.set_price('A', 50)
    shop.set_price('B', 30)
    shop.set_price('C', 20)
    shop.set_price('D', 15)

    shop.add_offer('A', 3, 130)
    shop.add_offer('B', 2, 45)

    checkout = Checkout(shop)

    for sku in skus:
        checkout.add_item(sku)

    print(checkout.get_total())
    return checkout.get_total()