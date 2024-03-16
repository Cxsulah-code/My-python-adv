class Person:
  def __init__(self, Fname, Lname, feeling): 
    self.Fname = Fname
    self.Lname = Lname
    self.feeling = feeling

  import datetime
  time = datetime.datetime.now()
    
  print(time.strftime("%A"))
  
  def greeting(self): 
    
    print(f"Hello {self.Fname} {self.Lname} are you feeling {self.feeling} at {self.time}")
    
ps1 = Person(Fname="Kizito", Lname="Sulah", feeling="blessed")

ps1.greeting()

class Man: 
  def __init__(self, name, feeling): 
    self.name = name
    self.feeling = feeling
    
  def __str__(self): 
    return f"Hi {self.name} am {self.feeling}"

#  def greet(self): 
    x = 13
    if x < 12: 
      return "Good Morning"
    elif x > 13 and x < 15: 
      return "Good Afternoon"
    else: 
      return "Good Evening"
    print(x)
      
man1 = Man(name="Kizito", feeling="cool")
      
#man1.greet()
print(man1)


