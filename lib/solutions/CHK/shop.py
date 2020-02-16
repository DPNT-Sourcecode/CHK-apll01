from .offer import FreebieOffer
from .offer import MultiOffer

class Shop(object):
    def __init__(self):
        self.prices = dict()
        self.free_offers = []
        self.multi_offers = []

    def set_price(self, sku, price):
        self.prices[sku] = price

    def get_price(self, sku):
        if sku in self.prices:
            return self.prices[sku]
        else:
            return -1

    def add_offer(self, sku, quantity, price_or_freebie):
        if type(price_or_freebie) == int:
            offer = MultiOffer(sku, quantity, price_or_freebie)
            self.multi_offers.append(offer)
        elif type(price_or_freebie) == str:
            offer = FreebieOffer(sku, quantity, price_or_freebie)
            self.free_offers.append(offer)

 
    def get_free_offers(self):
        return self.free_offers

    def get_multi_offers(self):
        return self.multi_offers