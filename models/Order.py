import models.Customer as c
class Orders:
    def __init__(self, order_id = 0, customer_name=c.Customers.name, products, total_price):
        self.order_id = order_id



    def setOrder(self, customer_name, products,total_price):
        self.customer_name = customer_name
        self.products = products
        self.total_price = total_price

    def getOrders(self):
        return (self.customer_name, self.products, self.total_price)