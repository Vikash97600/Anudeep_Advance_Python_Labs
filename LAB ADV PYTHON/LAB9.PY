# 1: Employee Salary Management (Abstraction) You are tasked with building an employee salary management system.
# Use abstraction to create a base class Employee and two subclasses, FullTimeEmployee and PartTimeEmployee.
# ● Abstract Class: Employee with abstract methods calculate_salary() and get_employee_details(). 
# ● FullTimeEmployee: Overrides calculate_salary() by considering a monthly fixed salary. 
# ● PartTimeEmployee: Overrides calculate_salary() by considering an hourly rate and hours worked. 

# Task: 1. Create the abstract class and its subclasses. 
# 2. Implement the salary calculation for both types of employees.
# 3. Instantiate both employee types, calculate salaries, and display their details.
# 4. Add an abstract method raise_salary() that forces both subclasses to implement their logic for raising the salary. 
'''
from abc import ABC, abstractmethod

# Create the abstract class Employee
class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def get_employee_details(self):
        pass

    @abstractmethod
    def raise_salary(self):
        pass


# Create the subclass FullTimeEmployee
class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

    def get_employee_details(self):
        return f"Full-Time Employee: {self.name}, ID: {self.employee_id}, Monthly Salary: ${self.monthly_salary}"

    def raise_salary(self, raise_amount):
        self.monthly_salary += raise_amount
        return f"Salary raised by ${raise_amount}. New monthly salary: ${self.monthly_salary}"


# Create the subclass PartTimeEmployee
class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def get_employee_details(self):
        return f"Part-Time Employee: {self.name}, ID: {self.employee_id}, Hourly Rate: ${self.hourly_rate}, Hours Worked: {self.hours_worked}"

    def raise_salary(self, raise_amount):
        self.hourly_rate += raise_amount
        return f"Hourly rate raised by ${raise_amount}. New hourly rate: ${self.hourly_rate}"


# Instantiate both employee types, calculate salaries, and display their details
# Create a FullTimeEmployee
full_time_employee = FullTimeEmployee("Vikash", "FT001", 5000)
print(full_time_employee.get_employee_details())
print(f"Calculated Salary: ${full_time_employee.calculate_salary()}")
print(full_time_employee.raise_salary(500))

print("\n")

# Create a PartTimeEmployee
part_time_employee = PartTimeEmployee("JHitesh", "PT001", 8, 150)
print(part_time_employee.get_employee_details())
print(f"Calculated Salary: ${part_time_employee.calculate_salary()}")
print(part_time_employee.raise_salary(2))

'''

# 2: Smart Home Devices (Encapsulation and Property Decorators) Develop a system to manage smart home devices.
# Implement a class SmartDevice that: 
# ● Uses encapsulation to store the device’s status (__is_on, default to False).
# ● Has a turn_on() and turn_off() method to change the device status.
# ● Uses a property decorator to expose the device’s status as a property (is_on) with a setter to prevent turning it on if certain conditions (like low battery) are met. 
# Task: 1. Implement the SmartDevice class. 
# 2. Simulate turning the device on and off while managing conditions like low battery.
# 3. Use the property method to ensure users cannot turn on the device when the battery is below a threshold.


class SmartDevice:
    def __init__(self):
        self.__is_on = False
        self.battery_level = 100  # Default battery level in percentage

    @property
    def is_on(self):
        return self.__is_on

    @is_on.setter
    def is_on(self, value):
        if value:  # Only check battery when turning on
            if self.battery_level < 20:
                print("Cannot turn on device: battery level is too low.")
                return
        self.__is_on = value

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False



device = SmartDevice()
    
# Low battery scenario
device.battery_level = 15
print(f"Battery level: {device.battery_level}%")
device.turn_on()
print(f"Device is on: {device.is_on}\n")  
    
# Charge the battery
device.battery_level = 85
print(f"Battery level: {device.battery_level}%")
device.turn_on()
print(f"Device is on: {device.is_on}\n")
    
# Turn off the device
device.turn_off()
print(f"Device is on: {device.is_on}")  