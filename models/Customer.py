class Customer:
    def __init__(self, customer_id=0, name="", contact=("", "")):
        self.__customer_id = customer_id
        self.__name = name
        self.__contact = contact

    # Accessor methods (getters)
    def get_customer_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name

    def get_contact(self):
        return self.__contact

    # Mutator methods (setters)
    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_name(self, name):
        self.__name = name

    def set_contact(self, contact):
        self.__contact = contact

    # Properties for accessors and mutators
    customer_id = property(get_customer_id, set_customer_id)
    name = property(get_name, set_name)
    contact = property(get_contact, set_contact)

def test_usage():
    # Usage example
    customer = Customer(1, "John Doe", ("john@example.com", "123-456-7890"))
    print(customer.get_customer_id())  # 1
    print(customer.get_name())  # John Doe
    print(customer.get_contact())  # ('john@example.com', '123-456-7890')

    customer.set_name("Jane Doe")
    print(customer.get_name())  # Jane Doe

if __name__ == "__main__":
    test_usage()