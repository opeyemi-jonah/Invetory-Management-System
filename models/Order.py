class Order:
    def __init__(self, order_id, customer_name, products, total_price=0.0):
        self.__order_id = order_id
        self.__customer_name = customer_name
        self.__products = products  # List of dictionaries with product_id and quantity
        self.__total_price = total_price

    # Accessor methods (getters)
    def get_order_id(self):
        return self.__order_id

    def get_customer_name(self):
        return self.__customer_name

    def get_products(self):
        return self.__products

    def get_total_price(self):
        return self.__total_price

    # Mutator methods (setters)
    def set_order_id(self, order_id):
        self.__order_id = order_id

    def set_customer_name(self, customer_name):
        self.__customer_name = customer_name

    def set_products(self, products):
        self.__products = products

    def set_total_price(self, total_price):
        self.__total_price = total_price

    # Properties for accessors and mutators
    order_id = property(get_order_id, set_order_id)
    customer_name = property(get_customer_name, set_customer_name)
    products = property(get_products, set_products)
    total_price = property(get_total_price, set_total_price)

    # Method to calculate total price based on products list
    def calculate_total_price(self, product_prices):
        self.__total_price = sum(product_prices[product['product_id']] * product['quantity'] for product in self.__products)
        return self.__total_price

def test_usage():
    # Usage example
    order = Order(
        order_id="O001",
        customer_name="John Doe",
        products=[{'product_id': 'P001', 'quantity': 2}, {'product_id': 'P002', 'quantity': 1}]
    )

    print(order.get_order_id())  # O001
    print(order.get_customer_name())  # John Doe
    print(order.get_products())  # [{'product_id': 'P001', 'quantity': 2}, {'product_id': 'P002', 'quantity': 1}]

    # Assuming product prices are provided as a dictionary
    product_prices = {'P001': 100.0, 'P002': 150.0}
    total_price = order.calculate_total_price(product_prices)
    print(total_price)  # 350.0
if __name__ == '__main__':
    test_usage()
