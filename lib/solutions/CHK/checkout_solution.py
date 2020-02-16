from .checkout import Checkout
from .shop import Shop

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    shop = Shop()
 
    price_list = [
        50,30,20,15,40,10,20,10,35,60,
        80,90,15,40,10,50,30,50,30,20,
        40,50,20,90,10,50
        ]

    for index, price in enumerate(price_list):
        shop.add_offer(chr(65+index) ,price)


    shop.add_offer('A', 5, 200)
    shop.add_offer('A', 3, 130)
    shop.add_offer('B', 2, 45)
    shop.add_offer('E', 2, 'B')
    shop.add_offer('F', 2, 'F')
    shop.add_offer('H', 10, 80)
    shop.add_offer('H', 5, 45)
    shop.add_offer('K', 2, 150)
    shop.add_offer('N', 3, 'M')
    shop.add_offer('P', 5, '200')
    shop.add_offer('Q', 3, 80)
    shop.add_offer('R', 3, 'Q')
    shop.add_offer('U', 3, 'U')
    shop.add_offer('V', 3, '130')
    shop.add_offer('V', 2, '90')

    checkout = Checkout(shop)

    for sku in skus:
        checkout.add_item(sku)
        
    return checkout.get_total()
