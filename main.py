x = "Hello "  
y = "sulah"
print( x+" "+y)
print()

# replication operator "*"
print(x* 3)
print()

#math module function
import math

a=4.6
print(math.ceil(a))
print(math.floor(a))
b=9
print(math.sqrt(b))
print(math.exp(3.0))
print(math.log(2.0))
print(math.pow(2.0,3.0))
print(math.sin(0))
print(math.cos(0))
print (math.tan(45))

print()

print("math.pi : ",math.pi)
print("math.e : ",math.e)

print()
# if statement
#grade = 70
#if grade >= 50:
  
#print("passed average mark")
#else:
#print("below average mark")


# else if or elif statement
grade= 94
if grade >= 90:
    print("A grade")
elif grade >=80:
    print("B grade")
elif grade >=70:
    print("C grade")
elif grade >= 65:
    print("D grade")
else:
    print("Failing grade")
print()
    
    #for loop
    
row=7
for i in range(row):
    for j in range (i):
         print(i,end=" ") #print number
    print(" ")
print()
#while loop

count = 0
while (count < 5): count += 1;
print("I am",count)

print()
#break statement

number = 0
for number in range(10):
   number = number + 1
   if number == 7:
      break # break here
   print('Number is ' + str(number))
print('Out of loop')

print()
#continue statement
a=0

while a<=5:
    a=a+1
    if a%2==0:
        continue
    print(a)
print("End of Loop")