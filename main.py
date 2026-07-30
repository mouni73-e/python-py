'''
#packgesa

from packages.student import student
from packages.marks import mark
print(student("name",11))
print(mark(23,45,76))

''

import pandas as pd
data = {
    "name" : ["name","name2","name3"],
    "age" : [22,23,24]
}

df = pd.DataFrame(data)
print(df)

''

import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [5,8,6,10]

plt.plot(x,y)
plt.title("student Marks")
plt.xlabel("students")
plt.ylabel("marks")
plt.show()

''
import pygame
pygame.init()
screen = pygame.dispaly.set_mode((500,500))
pygame.dispaly.set_caption("My Game")
pygame.draw.circle(screen,(250,0),(250,250),500)
pygame.display.filp()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

''
#itteraters
nums = [10,20,30]
it = iter(nums)

print(next(it))
print(next(it))
print(next(it))

'''

class count:
    def __init__(self,start):
        self.current = start
    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val
for n in count(5):
    print(n)


