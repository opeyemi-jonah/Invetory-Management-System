class Products:
    def __init__(self, product_id, name = "", category = "", price = 0 , quantity = 0,total_sum = 0):
        self.__product_id = product_id
        self.__name = name
        self.__category = category
        self.__price = price
        self.__quantity = quantity
        self.__total_sum = total_sum

# Mutator & Accessor


    def getProducts(self):
        return (self.name, self.category, self.price, self.quantity)
    
    def total_price(self, list_of_prices):
        for price in list_of_prices:
            self.total_sum += int(price)
            print(self.total_sum)
        return self.total_sum

