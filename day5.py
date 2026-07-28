class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


s = Student("Mamatha", 22)
s.display()

.............

class Bank:
    def __init__(self, balance):
        self.__balance = balance 

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Balance:", self.__balance)


b = Bank(10000)

b.show_balance()
b.deposit(2000)
b.show_balance()
b.withdraw(5000)
b.show_balance()

.............

class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.pi * self.radius ** 2


c = Circle(5)
print(c.area())

...........

class father:
    def display(self):
        print("this is a parent class")
class mother():
    def show(self):
        print("this is a child class")

class child(father,mother):
    def show1(self):
         print("this is multipule inheristance")

obj = child()
obj.display()
obj.show()
obj.show1()

............

class Employee:
    def __init__(self, name, emp_id, salary, dept):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        self.dept = dept

    def display(self):
        print(f"{self.name} is working in {self.dept} department and is getting a salary of {self.salary}.")


name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
salary = int(input("Enter Salary: "))
dept = input("Enter Department: ")

e = Employee(name, emp_id, salary, dept)
e.display()

........

class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.name)


class Developer(Employee):
    def __init__(self, emp_id, name, language, team_size):
        super().__init__(emp_id, name)
        self.language = language
        self.team_size = team_size

    def display(self):
        super().display()
        print("Programming Language:", self.language)
        print("Team Size:", self.team_size)


d = Developer(101, "Mamatha", "Python", 8)
d.display()

.......

lass Camera:
    def capture_image(self):
        print("Capturing image...")


class Phone:
    def calling(self):
        print("Calling...")


class iPhone(Camera, Phone):
    def info(self):
        print("iPhone features")


i = iPhone()
i.info()
i.capture_image()
i.calling()

.......

class parent:
    def display(self):
        print("this is a parent class")

class child(parent):
     def show(self):
         print("this is a child class")

obj = child()
obj.display()
obj.show()

.......

class product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def display(self):
        print(f'product: {self.name}')
        print(f'price: {self.price}')


class clothing(product):
        def __init__(self, name, price,warranty):
             super().__init__(name,price)
             self.warranty = warranty

        def display(self):
            self.display
            print(f'warranty:{self.warranty}years')

l = clothing('shirt',2000,1)
l.display()

......

class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def change_pi(cls, value):
        cls.pi = value

    @staticmethod
    def info():
        print("This program calculates the area of a circle.")

    def area(self):
        return Circle.pi * self.radius ** 2


Circle.info()          # Static method
Circle.change_pi(3.14) # Class method

c = Circle(5)
print("Area of circle =", c.area())

............

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)


s1 = Student("Mamatha", 101)

s1.display()

.........

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


t = Triangle(10, 5)
print("Area of triangle =", t.area())

...........

class father:
    def display(self):
        print("this is a parent class")
class mother():
    def show(self):
        print("this is a child class")

class child(father,mother):
    def show1(self):
         print("this is multipule inheristance")

obj = child()
obj.display()
obj.show()
obj.show1()
