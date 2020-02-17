import operator

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
        free_offers = self.shop.get_free_offers()
        multi_offers = self.shop.get_multi_offers()

        #apply free offers first
        for free_offer in free_offers:
            sku = free_offer.get_sku()
            sku_price = self.shop.get_price(sku)
            if sku_price == -1:
                return -1
            quantity = free_offer.get_quantity()
            freebie_sku = free_offer.get_free_sku()
            if sku in items and freebie_sku in items:
                while quantity <= items[sku] and items[freebie_sku]>0:
                    total += quantity*sku_price
                    items[sku]-= quantity
                    items[freebie_sku]-=1

        #apply multibuy next - biggest to smallest
        for multi_offer in multi_offers:
            sku = multi_offer.get_sku() 
            quantity = multi_offer.get_quantity()   
            multi_price = multi_offer.get_price()      
            if type(sku) == list:
                sku_list= []
                for item in sku:
                    if item in items:
                        for x in range(items[item]):
                            if self.shop.get_price(sku_list[0]) >= self.shop.get_price(item):
                                sku_list.append(item)
                            else:
                                sku_list.insert(0,item)
                
                while quantity<= len(sku_list):        
                    total += multi_price
                    for i in range(quantity):
                        items[sku_list[0]]-=1
                        sku_list.pop(0)

            elif sku in items:
                while quantity<= items[sku]:
                    total += multi_price
                    items[sku] -= quantity

        #calculate rest of checkout
        for sku in items:
            sku_price = self.shop.get_price(sku)
            if sku_price == -1:
                return -1
            if items[sku] >=0: total=total+(items[sku]*sku_price)

        return(total)