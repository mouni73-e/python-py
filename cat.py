'''
class animal:
    def sound(self):
        print("animal sound")

class dog(animal):
    def sound(self):
        print("Bark")

class cat(animal):
    def sound(self):
        print("Meow")

d = dog()
c = cat()

d.sound()
c.sound()

'''''''
class dog():
    def sound(self):
        print("bark")

class cat:
    def sound(self):
        print("Meow")

def make_sound(animal):
    animal.sound()

make_sound(dog())
make_sound(cat())

''
class cal:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c
    
obj = cal()
print(obj.add(10,20,30))

''
# method over lodaing
class cal:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c,d=0):
        return a+b+c+d
    
obj = cal()
print(obj.add(10,20,30,40))

''

#abstract method
from abc import ABC, abstractmethod

class shape(ABC):
    def area(self):
        pass

class rectangle(shape):

    def __init__(self,l,b):
        self.l = l
        self.b = b

    def area(self):
        print(self.l*self.b)

r = rectangle(10,5)

r.area()

''
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self, r):
        self.r = r

    def area(self):
        print(3.14 * self.r * self.r)

c = Circle(7)

c.area()

''

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Triangle(Shape):

    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        print(0.5 * self.b * self.h)

t = Triangle(10, 6)

t.area()

''

import module

print(module.add(10,20))
print(module.multiply(10,20))

''

from module import *
print(add(10,20))
print(multiply(10,20))

''
import math
print(math.sqrt(25))
print(math.ceil(25.5))
print(math.floor(25.5))
print(math.pi)

''
import os
print(os.getcwd)
print(os.listdir)
print(os.mkdir('new floder'))

'''

from datetime import datetime,date,timedelta
now = datetime.now()
print(now.year,now.month,now.day)
print(now.strftime('%H : %M : %S'))
today = date.today()
print(today)
tomorrow = today + timedelta(days= 3)
print(tomorrow)
diff = datetime(2025,1,1) - datetime.now()
print(diff)


