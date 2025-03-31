# 1: Scenario:
# You are tasked with developing a hospital management system that
# handles different types of hospital staff:

# Doctors, Nurses, and Administrative Staff. Each
# type of staff member has basic details such as name, ID, and department. Doctors have
# specializations, nurses have shifts, and administrative staff have roles. The system
# should allow you to display staff information and also calculate their monthly salaries
# based on their unique attributes.


class Staff:
    def __init__(self, name, id, dept):
        self.name = name
        self.id = id
        self.dept = dept

    def display_info(self):
        print(f"ID: {self.id}, Name: {self.name}, Department: {self.dept}")

    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement calculate_salary")


class Doctor(Staff):
    def __init__(self, name, id, department, specialization):
        super().__init__(name, id, department)
        self.specialization = specialization

    def display_info(self):
        super().display_info()
        print(f"Specialization: {self.specialization}")

    def calculate_salary(self):
        base = 5000
        if self.specialization == "Surgeon":
            return base + 3000
        elif self.specialization == "Neurologist":
            return base + 1000
        else:
            return base + 2000


class Nurse(Staff):
    def __init__(self, name, id, department, shift):
        super().__init__(name, id, department)
        self.shift = shift

    def display_info(self):
        super().display_info()
        print(f"Shift: {self.shift}")

    def calculate_salary(self):
        if self.shift == "morning":
            return 3000
        elif self.shift == "evening":
            return 3200
        elif self.shift == "night":
            return 3500
        else:
            return 3000


class Admin(Staff):
    def __init__(self, name, id, department, role):
        super().__init__(name, id, department)
        self.role = role

    def display_info(self):
        super().display_info()
        print(f"Role: {self.role}")

    def calculate_salary(self):
        roles = {
            "HR": 4000,
            "Finance": 4500,
            "Receptionist": 3500
        }
        return roles.get(self.role, 3500)


# Example usage
doc = Doctor("Dr.Vikash", "D001", "Cardiology", "Surgeon")
doc.display_info()
print("Salary:", doc.calculate_salary())
nurse = Nurse("Anchal", "N001", "ER", "night")
nurse.display_info()
print("Salary:", nurse.calculate_salary())
admin = Admin("Hitesh", "A001", "Admin", "HR")
admin.display_info()
print("Salary:", admin.calculate_salary())

# 2. : Vehicle Rental System
# Imagine you are developing a Vehicle Rental System where different types of vehicles
# (like Car, Bike, and Truck) are available for rent.
# ● All vehicles have some common attributes like registration_number, brand, and rental_price_per_day.
# ● Each type of vehicle has a different pricing strategy. For example, trucks have
# additional charges for heavy loads, and cars have insurance fees included.
# Task:
# ● Design a class Vehicle with a method calculate_rental_cost(), which will be overridden in the subclasses
# Car, Bike, and Truck.
# ● Use method overriding to customize the rental cost calculation for each vehicle

# type.
# ● Use the super() method to access common attributes from the Vehicle class.


class Vehicle:
    def __init__(self, registration_number, brand, rental_price_per_day):
        self.registration_number = registration_number
        self.brand = brand
        self.rental_price_per_day = rental_price_per_day

    def calculate_rental_cost(self, days):
        return self.rental_price_per_day * days


class Car(Vehicle):
    def __init__(self, registration_number, brand, rental_price_per_day, insurance_fee_per_day):
        super().__init__(registration_number, brand, rental_price_per_day)
        self.insurance_fee_per_day = insurance_fee_per_day

    def calculate_rental_cost(self, days):
        base_cost = super().calculate_rental_cost(days)
        insurance_cost = self.insurance_fee_per_day * days
        return base_cost + insurance_cost


class Bike(Vehicle):
    def __init__(self, registration_number, brand, rental_price_per_day, helmet_rental_fee_per_day):
        super().__init__(registration_number, brand, rental_price_per_day)
        self.helmet_rental_fee_per_day = helmet_rental_fee_per_day

    def calculate_rental_cost(self, days):
        base_cost = super().calculate_rental_cost(days)
        helmet_cost = self.helmet_rental_fee_per_day * days
        return base_cost + helmet_cost


class Truck(Vehicle):
    def __init__(self, registration_number, brand, rental_price_per_day, heavy_load_charge_per_day):
        super().__init__(registration_number, brand, rental_price_per_day)
        self.heavy_load_charge_per_day = heavy_load_charge_per_day

    def calculate_rental_cost(self, days, is_heavy_load=False):
        base_cost = super().calculate_rental_cost(days)
        if is_heavy_load:
            heavy_cost = self.heavy_load_charge_per_day * days
            return base_cost + heavy_cost
        return base_cost


# Create instances
car = Car("CAR123", "Toyota", 50, 10)
bike = Bike("BIKE456", "Giant", 20, 5)
truck = Truck("TRUCK789", "Ford", 80, 20)

# Calculate costs
print(car.calculate_rental_cost(3))          
print(bike.calculate_rental_cost(2))         
print(truck.calculate_rental_cost(2))        
print(truck.calculate_rental_cost(2, True))  