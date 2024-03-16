## input statement....

rows = int(input("Enter the n of rows: "))
columns = int(input("Enter the n of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
  for y in range(columns):
    print(symbol,end=" ")
  print()
print()

def cube(x):
    return x*x*x

a=int(input("Enter number :"))
print("cube of ",a," is ",cube(a))

print()

