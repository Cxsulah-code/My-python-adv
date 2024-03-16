print("Hello class")
print()
class Person: 
  def __init__(self, name, age, school, grade): 
    self.name = name
    self.age = age
    self.school = school
    self.grade = grade
    
  def __str__(self): 
    return f"{self.name} is {self.age} and goes to {self.school}"
  def greet(self): 
    print(f"Hello {self.name} at {self.school} in {self.grade} grade.")

p1 = Person("Rashid", 20, "Itty bities nursery school.", "5")

class Pupil(Person): 
  def __init__(self, name, age, school, grade): 
    super().__init__(name, age, school, grade)

class Nursery(Pupil): 
  def __init__(self, name, age, school, grade): 
    super().__init__(name, age, school, grade)  
    
chld1 = Nursery(name="Rashid", age="14", school="Stahuza junior school", grade="3")    
  
print(p1.name)
print(p1)

chld1.greet()