## Method Overriding  (Run-time Polymorphism)

#when a sub class creates a same name function as in parent class
class animals():
    def __init__(self,name):
     self.name=name
    
class dog(animals):
   def sound(self):
       print("Whoah Whoah!")
class cat(animals):
   def sound(self):
       print("Meow Meow!")
class goat(animals):
   def sound(self):
      print("mee mee mee!")


a1=dog("max")
a1.sound()

a2=cat("lina")
a2.sound()

a3=goat("belli")
a3.sound()

print(a3.name)


## Method Overrriding (Compile time polymorphism)

# same method name in a single class with different parameter.


class add_num:
   def add(self, a=0, b=0):
      if isinstance(a,int) and isinstance(b,int):
         print("This is an int.")
      elif isinstance(a,str) and isinstance(b,str):
         print("This is an String.")
      elif isinstance(a,float) and isinstance(b,float):
         print("This is an float.")



   

num=add_num()
num.add("2","4")

num2=add_num()
num2.add(45,15)

num3=add_num()
num2.add(3.5,2.6)  



## Duck Typing ( In duck type the object type doesn't matter if the work is same)

class laptop:
   def code(self):
      print("I am coding on laptop.")
class computer:
   def code(self):
      print("I am coding on Computer.")
class Mobile:
   def code(self):
      print("I am coding on Mobile")
  
def device_name(device):
   device.code()


device_name(laptop()) # we pass the class in this parameter which calls the code object in it for each device.
device_name(computer())
device_name(Mobile()) 

#  Opertaor overriding ( special method)
class  Number:
   def __init__(self,value):
      self.value=value
   def __add__(self,others): # def __add__ overides the add with inside operator
       return Number(self.value*others.value)
   def show(self):
      print("Value:",self.value)

value1=Number(10)
value2=Number(30)
value3=value1+value2   #It override the operator I add the value but it didn't add instead it multiply by magic method.
value3.show()

value4=value3+value1 # It wil give ans 3000 as it overides the + operator and goes into multiply method.
value4.show()
 