class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance = self.__balance - amount
            print("Withdrawal Successful")
            print("Remaining Balance:", self.__balance)
        else:
            print("Insufficient Balance")

account = BankAccount(10000)

account.withdraw(3000)

account.withdraw(9000)

......

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print("Balance:", self.__balance)

account = BankAccount(5000)

account.show_balance()

try:
    print(account.__balance)
except AttributeError:
    print("AttributeError (when accessed directly)")

    ......

class Animal:
    def eat(self):
        print("Animal eats food")

class Bird(Animal):
    def fly(self):
        print("Birds can fly")

class Parrot(Bird):
    def speak(self):
        print("Parrot can speak")

p = Parrot()

p.eat()
p.fly()
p.speak()

......


class Camera:
    def take_photo(self):
        print("Taking photo")

class MusicPlayer:
    def play_music(self):
        print("Playing music")

class SmartPhone(Camera, MusicPlayer):
    def calling(self):
        print("Calling...")

phone = SmartPhone()

phone.take_photo()
phone.play_music()
phone.calling()

.....

class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age


class student1(student):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)

        
d = student1("Mamatha", 30, 50000)
d.display()

......

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s = Student("Mamatha", 95)

print("Name:", s.name)
print("Marks:", s.marks)

.....

class wallet:
    def __init__(self, balance):
        self.__balance = balance   

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def show_money(self):
        print("Money Available:", self.__balance)

account = wallet(1000)

account.deposit(500)

account.show_money()


