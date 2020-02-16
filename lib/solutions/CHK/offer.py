class Offer(object):
    def __init__(self,sku,quantity):
        self.sku = sku
        self.quantity = quantity
    
    def get_sku(self):
        return self.sku

    def get_quantity(self):
        return self.quantity

class MultiOffer(Offer):
    def __init__(self, sku, quantity, price):
        super().__init__(sku, quantity)
        self.price = price

    def get_price(self):
        return self.price
    
class FreebieOffer(Offer):
    def __init__(self, sku, quantity, free_sku):
        super().__init__(sku, quantity)
        self.free_sku = free_sku

    def get_free_sku(self):
        return self.free_sku