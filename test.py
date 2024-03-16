
# Nested for loop
row=9
for i in range(row):
    for j in range (i):
        print(i,end=" ") #print number
    print(" ")
print()
    
# fibonacci numbers
    
from fib import fib
print(fib(100))
print()
    
#example ----2
row=6
for i in range (row):
    for j in range (5,i-1,-1):
        print("*",end=" ") # print * and space
    print(" ")
print()
     
print(".....########.......")
print()

for i in range(3):
  for j in range (1, 10):
    print(j,end=" ")   
  print()
  
print()