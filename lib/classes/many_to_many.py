class Coffee:
    coffee_list = []

    def __init__(self, name):
        self.name = name
        self._orders = []
        Coffee.coffee_list.append(self)

    def get_coffee(self):
        return self._name
    def set_coffee(self, value):
        if type(value) is str and len(value) >= 3 and not hasattr(self, '_name'):
            self._name = value
        else:
            None
    name = property(get_coffee, set_coffee)
    
    def orders(self):
        orders = []
        for order in Order.all:
            if order.coffee is self:
                orders.append(order)
        return orders
                
    def customers(self):
        set_customer = set()
        for order in Order.all:
            if order.coffee is self:
                set_customer.add(order.customer)
        return list(set_customer)
                
    def num_orders(self):
        num_orders = 0
        for order in Order.all:
            if order.coffee is self:
                num_orders += 1
        return num_orders
    
    def average_price(self):
        my_orders = self.orders()
        if len(my_orders) == 0:
            return 0
        sum = 0
        for order in my_orders:
            sum += order.price
        return sum/len(my_orders)

class Customer:
    customer_list = []

    def __init__(self, name):
        self.name = name
        self._orders = []
        Customer.customer_list.append(self)

    def get_name(self):
        return self._name
    def set_name(self, value):
        if type(value) is str and 1 <= len(value) <= 15:
            self._name = value
        else:
            None
    name = property(get_name, set_name)
        
    def orders(self):
        order_list = []
        for order in Order.all:
            if order.customer is self:
                order_list.append(order)
        return order_list
    
    def coffees(self):
        r_l = set()
        for order in Order.all:
            if order.customer is self:
                r_l.add(order.coffee)
        return list(r_l)
    
    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self._orders.append(order)
        Order.all.append(order)
        return order
    
class Order:
    all = []
    order_list =[]

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    def get_price(self):
        return self._price
    def set_price(self, value):
        if type(value) is float and 1 <= float(value) <= 10 and not hasattr(self, 'price'):
            self._price = value
        else:
            None
    price = property(get_price, set_price)

    def customer_order(self):
        for customer in Customer.customer_list:
            if customer == self.customer:
                customer.customer_order_list.append(self)

    def coffee_order(self):
        for coffee in Coffee.coffee_list:
            if coffee == self.coffee:
                coffee.orderz.append(self)
