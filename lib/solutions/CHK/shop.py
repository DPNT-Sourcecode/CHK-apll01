class Shop(object):
    self __init__(self):
        self.prices = dict()
        self.offers = dict()

    def set_price(self, sku, price){
        self.prices[sku] = price
    }

    def get_price(self, sku){
        return self.prices[sku]