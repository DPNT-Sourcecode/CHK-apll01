class Shop(object):
    def __init__(self):
        self.prices = dict()
        self.offers = dict()

    def set_price(self, sku, price){
        self.prices[sku] = price
    }

    def get_price(self, sku){
        return self.prices[sku]

    def add_offer(self, sku, quantity, price){
        offer = (sku, quantity, price)
        self.offers[sku] = offer
    }

    def get_offers(self){
        return self.offers
    }