
import math

a = float(input("a; "))
b = float(input("b; "))
c = float(input("c; "))

discrmnt = math.pow(b, 2) - (4 * a * c)

if discrmnt > 0: 

   x1 = (((-b) + (math.sqrt(discrmnt))) / (2 * a))
   x2 = (((-b) - (math.sqrt(discrmnt))) / (2 * a))
   print("The're 2 roots: x1 and x2 =" , (x1, x2))
elif discrmnt ==0: 
  
   x = (-b) / (2 * a)
   print("The're is 1 roots", x)
  
else: 
   print("No roots, discrmnt < 0")