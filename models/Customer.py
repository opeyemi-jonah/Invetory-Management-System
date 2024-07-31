class Customers:
    def __init__(self, customer_id=0, name="", contact=("","")):
        self.__customer_id = customer_id
        self.__name = name
        self.__contact = contact
    
    # Customer ID Mutator & Accessor
    def get_customer_id(self):
        return self.__customer_id
    
    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id
    
    customer_id = property(get_customer_id, set_customer_id)
    
    # Name Mutator & Accessor
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    name = property(get_name, set_name)
    
    
    # Contact Mutator & Accessor
    def get_contact(self):
        return self.__contact
    
    def set_contact(self, contact):
        self.__contact = contact

    contact = property(get_contact, set_contact)
    