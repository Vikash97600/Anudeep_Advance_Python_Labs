# Question 1 

# Program:


class Product:
    total_products = 0

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        Product.total_products += 1

    def update_stock(self, quantity):
        self.stock += quantity

    def display_info(self, basic=True):
        if basic:
            return f"Name of the product: {self.name}, Price of the product: {self.price}, Number of stocks: {self.stock}"
        else:
            return f"Name of the product: {self.name}, Price of the product: {self.price}"

    @staticmethod
    def product_info():
        return "Products are available for purchase."

    @classmethod
    def get_total_products(cls):
        return cls.total_products


class Customer:
    customer_count = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.order_history = []
        Customer.customer_count += 1

    def place_order(self, order):
        self.order_history.append(order)

    @staticmethod
    def customer_info():
        return "Customers place orders and purchase products."

    @classmethod
    def get_customer_count(cls):
        return cls.customer_count


class Order:
    order_count = 0

    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.products = {}
        Order.order_count += 1

    def add_product(self, product, quantity):
        if product.stock >= quantity:
            self.products[product] = quantity
            product.update_stock(-quantity)
        else:
            print(f"Not enough stock for {product.name}")

    @staticmethod
    def order_info():
        return "Orders contain products purchased by customers."

    @classmethod
    def get_order_count(cls):
        return cls.order_count


    

#  2. Test the Classes: Create instances of Product, Customer, and Order. 
# Add products to the inventory, create orders, and place them for customers. 
# Use the method overloading simulation to display product details in different formats. 
# Call static methods to get general information and class methods to get counts. 

# Program:


# Test the Classes
product1 = Product("Laptop", 1000, 10)
product2 = Product("Phone", 500, 20)

customer1 = Customer("Alice", "alice@example.com")

order1 = Order(1, customer1)
order1.add_product(product1, 2)
order1.add_product(product2, 1)

customer1.place_order(order1)

print(product1.display_info())  # Basic info
print(product1.display_info(basic=False))  # Detailed info

print(Product.product_info())
print(Customer.customer_info())
print(Order.order_info())

print("Total Products:", Product.get_total_products())
print("Total Customers:", Customer.get_customer_count())
print("Total Orders:", Order.get_order_count())
