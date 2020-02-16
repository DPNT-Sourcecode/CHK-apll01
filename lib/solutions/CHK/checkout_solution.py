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
    shop.set_price('E', 40)
    shop.set_price('F', 10)

    shop.add_offer('A', 5, 200)
    shop.add_offer('A', 3, 130)
    shop.add_offer('B', 2, 45)
    shop.add_offer('E', 2, 'B')
    shop.add_offer('F', 2, 'F')

    checkout = Checkout(shop)

    for sku in skus:
        checkout.add_item(sku)
        
    return checkout.get_total()