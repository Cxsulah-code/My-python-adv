print("Hello Sulah")
print()


print("finding Area of a circle;")
import math
x = math.pi

def findArea(r): 
  
  return x * (math.pow(r,2));
  
print("Area of a circle =" , findArea(5));  

print()

def findVolume(r): 
  
  return x * (math.pow(r,3));
  
print("Volume of a sphere =", findVolume(6));

print()
#print("Elijjah's ans =",math.sqrt(2500))

for row in range (7-1, -1, -1): 
  for col in range (7-row-1): 
    print(" ", end="")
    if row==0 or row==col or (row+col==6): 
      print (col+1, end="")
    else: 
      print("*", end="")
  print()
  
print()
n = int(input("Enter any number; "))
for i in range (n-1, -1, -1): 
  for j in range (n-i-1): 
    print(" ", end="")
  for j in range (i, -1, -1): 
    print(n-j, end=" ")
  print()  
for i in range (n): 
  for j in range (n-i-1): 
    print(" ", end="")
  for j in range (i+1): 
    print(n-j, end=" ")
  print()  
  
print("My inverted pyramid")  
print()
for i in range (6-1, -1, -1): 
  for j in range (6-i-1): 
    print(" ", end="")
  for j in range (i, -1, -1): 
    print("*", end=" ")
  print()  

print()
n = int(input("Enter ur number; "))
#for i in range (n-1, -1, -1):
for i in range (n):   
  for j in range (n-i-1): 
    print(" ", end="")
  for j in range (i, -1, -1): 
    print(n-i, end=" ")
  print()  
  
print()
n = input("Enter ur name; ")
x = ""
for i in n: 
  x += i
  print(x)