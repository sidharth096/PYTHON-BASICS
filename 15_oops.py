# Object-Oriented Programming (OOP) in Python

# 1. Class and Object
class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age

    # Method
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object
person1 = Person("Ram", 25)
person1.greet()

print("=========================")

# 2. Inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # calling parent constructor
        self.student_id = student_id

    def display_id(self):
        print(f"My student ID is {self.student_id}")

student1 = Student("Sita", 20, "S123")
student1.greet()
student1.display_id()

print("=========================")

# 3. Encapsulation (hiding data)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print("Current Balance:", account.get_balance())

print("=========================")

# 4. Polymorphism
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

# Using polymorphism
animals = [Dog(), Cat()]
for animal in animals:
    animal.sound()
