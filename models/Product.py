class Products:
    def __init__(self, product_id, name="", category="", price=0, quantity=0, total_sum=0):
        self.__product_id = product_id
        self.__name = name
        self.__category = category
        self.__price = price
        self.__quantity = quantity
        self.__total_sum = total_sum

    # Accessor methods (getters)
    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_category(self):
        return self.__category

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def get_total_sum(self):
        return self.__total_sum

    def get_products(self):
        return (self.__name, self.__category, self.__price, self.__quantity)

    # Mutator methods (setters)
    def set_name(self, name):
        self.__name = name

    def set_category(self, category):
        self.__category = category

    def set_price(self, price):
        self.__price = price

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_total_sum(self, total_sum):
        self.__total_sum = total_sum

    # Method to calculate total price
    def total_price(self, list_of_prices):
        self.__total_sum = sum(int(price) for price in list_of_prices)
        return self.__total_sum

def test_usage():
    # Usage example
    product = Products("P001", "Laptop", "Electronics", 1000, 10)
    print(product.get_products())  # ('Laptop', 'Electronics', 1000, 10)

    product.set_price(1200)
    print(product.get_price())  # 1200

    total = product.total_price([100, 200, 300])
    print(total)  # 600

if __name__ == "__main__":
    test_usage()