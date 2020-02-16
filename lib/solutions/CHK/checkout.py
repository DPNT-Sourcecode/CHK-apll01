class Checkout(object):
    def __init__(self, shop):
        self.shop = shop
        self.items = dict()

    def add_item(self, sku):
        if sku in self.items:
            self.items[sku] += 1
        else:
            self.items[sku] = 1

    def remove_item(self, sku):
        if sku in self.items:
            self.items[sku] -= 1
            if self.items[sku] == 0:
                self.items.pop(sku)    

    def get_total(self):
        total = 0
        items = self.items.copy()
        offers = self.shop.get_offers()

        for sku in items:
            price = self.shop.get_price(sku)
            if price == -1:
                return -1
            else:
                total=total+(items[sku]*price)

