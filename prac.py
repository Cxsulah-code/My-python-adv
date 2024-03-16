class Man: 
  def __init__(self, name, age): 
    self.name = name
    self.age = age
    
p1 = Man("Sulah", 22)

print(p1.name, p1.age)

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
print()

for i in range (8, -1, -1): 
  for j in range (8-i-1, -1, -1): 
    print(" ", end="")
  for j in range (0, i): 
    print(i-j, end=" ")
  print()  
print()

for row in range (6): 
  for col in range (7): 
    if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8): 
      print("#", end="")
    else: 
      print(" ", end="")
  print()
  
import math as mx
#print(mx.log(100))

#import numpy as np
#x = np.array([1, 2, 3, 4, 5])
#print(x)
