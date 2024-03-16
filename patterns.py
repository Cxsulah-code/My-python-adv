## Learning different pattern and shapes
print("Patterns")
print()

n = int(input("Enter n of rows needed;"))
for i in range(n): 
  for j in range(n-i-1): 
# if i end=" ", returns a right-angled tri, bt if i end="", returns a pyramid.  
    print(" ", end="")
  for j in range(i+1): 
    print(j+1, end=" ")
  print()
  
print()

print("This is a pyramid...")
for i in range(7):
  for j in range(i-1, -1): #rangr(i-1, 0,-1)
     print(" ", end="")
  for k in range(0, i):
     print("#", end=" ")
  print(" ")

print()

pyramid_width = 4
for i in range(0, pyramid_width):
  for j in range(0, pyramid_width-i-1):
     print(" ", end="")
  for k in range(0, 2 * i + 1):
     print("@", end="")
  print(" ")
  
print()  
#number pattern
num = int(input("Enter n of rows; "))
for i in range(1, num+1):
  for j in range(1, num-i+1):
    print(end=" ")
  for j in range(i,0,-1):
    print(j,end="")
  for j in range(2,i+1):
    print(j,end="")
  print()
  
print()

print("This is a pyramid...")

for i in range(0, 7): 
  for j in range(0, 7-i-1): 
    print("*", end=" ")
    
  print(" ")
  
print()

n = int(input("Enter triangle rows; "))

for row in range (0, n): 
  for col in range (0, n): 
    if row==0 or col==(n-1) or row==col: 
      print("t", end="")
    else: 
      print(end=" ")
  print()
  
print()

for row in range (6): 
  for col in range (7): 
    if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8): 
      print("*", end="")
    else: 
      print(" ", end="")
  print()

string = input("Enter the string; ")
length = len(string)
for row in range (length): 
  for col in range (row+1): 
    print(string[col], end="")
  print()
  
print()
row = 5
for i in range (0, row + 1): 
  for j in range (row - i, 0, -1): 
    print(j, end="")
  print()