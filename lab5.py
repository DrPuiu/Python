#Exercitiul 1
import math

class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius**2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

#Exercitiul 2
class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"Account Balance for {self.account_holder}: ${self.balance}")

class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest calculated: ${interest}. New balance: ${self.balance}")

class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=100):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or overdraft limit exceeded.")


#exercitiul 3
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency 

    def calculate_mileage(self, distance):
        return distance / self.fuel_efficiency

class Motorcycle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def wheelie(self):
        return "Performing a wheelie!"

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity 

    def calculate_towing_capacity(self):
        return f"Towing capacity: {self.towing_capacity} pounds"

#Exercitiul 4
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: ${self.salary}"

class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

    def display_info(self):
        return super().display_info() + f", Department: {self.department}"

    def conduct_meeting(self):
        return "Conducting a meeting"

class Engineer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def display_info(self):
        return super().display_info() + f", Programming Language: {self.programming_language}"

    def write_code(self):
        return "Writing code"

class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, sales_target):
        super().__init__(name, employee_id, salary)
        self.sales_target = sales_target

    def display_info(self):
        return super().display_info() + f", Sales Target: ${self.sales_target}"

    def make_sale(self):
        return "Making a sale"


#Exercitiul 5
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass  

    def move(self):
        pass  

class Mammal(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color

    def give_birth(self):
        return f"{self.name} is giving birth to live young."

    def make_sound(self):
        return "Mammal sound"

    def move(self):
        return "Walking on four legs"

class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan

    def lay_eggs(self):
        return f"{self.name} is laying eggs."

    def make_sound(self):
        return "Bird sound"

    def move(self):
        return "Flying with wings"

class Fish(Animal):
    def __init__(self, name, species, scale_color):
        super().__init__(name, species)
        self.scale_color = scale_color

    def lay_eggs(self):
        return f"{self.name} is laying eggs."

    def make_sound(self):
        return "Fish sound"

    def move(self):
        return "Swimming in water"


#exercitiul 6
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass 

    def move(self):
        pass  

class Mammal(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color

    def give_birth(self):
        return f"{self.name} is giving birth to live young."

    def make_sound(self):
        return "Mammal sound"

    def move(self):
        return "Walking on four legs"

class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan

    def lay_eggs(self):
        return f"{self.name} is laying eggs."

    def make_sound(self):
        return "Bird sound"

    def move(self):
        return "Flying with wings"

class Fish(Animal):
    def __init__(self, name, species, scale_color):
        super().__init__(name, species)
        self.scale_color = scale_color

    def lay_eggs(self):
        return f"{self.name} is laying eggs."

    def make_sound(self):
        return "Fish sound"

    def move(self):
        return "Swimming in water"

mammal = Mammal(name="Lion", species="Panthera leo", fur_color="Golden")
print(mammal.give_birth())
print(mammal.move())

bird = Bird(name="Eagle", species="Aquila chrysaetos", wingspan=6.5)
print(bird.lay_eggs())
print(bird.move())

fish = Fish(name="Clownfish", species="Amphiprioninae", scale_color="Orange")
print(fish.lay_eggs())
print(fish.move())
