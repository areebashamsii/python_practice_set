## Class is a blueprint of object properties: ##

#Creating an empty class:

class person():
    pass # this keyword is used to create an empty class , not to get the error.



## Creating a pateint class ##
class pateint():
    def __init__(self,pateint_id,pateint_name,age,disease,bill_amount,admit_date,check_out_date):
       # __init__ is a special method use to create a constructor , it calls automatically when you iniialze an object
       self.pateint_id=pateint_id
       self.pateint_name=pateint_name
       self.age=age
       self.disease=disease
       self.bill_amount=bill_amount
       self.admit_date=admit_date
       self.check_out_date=check_out_date #A pateint class that has all the property column needed in pateint records

    def pateint_info(self):
        print(f"Pateint ID:",self.pateint_id)
        print(f"Pateint Name:",self.pateint_name)
        print(f"Age:",self.age)
        print(f"Bill Amount:",self.bill_amount)
        print(f"Admit Date:",self.admit_date)
        print(f"Check_out Date:",self.check_out_date)
        print("\n")


       # (SELF) is used to call the current object

## Creating object using class ##

      # object is an entity create by using a class.

p1=pateint(101,"Saleem",45,"fever",2300,"2025-06-21","2025-06-22")
p1.pateint_info()


## Mltiple objects using a class ##
p2=pateint(102,"shabana",52,"stomach pain",5000,"2025-06-23","2025-06-25")
p3=pateint(103,"Ali",52,"Chest pain",3000,"2025-06-23","2025-06-24")
p4=pateint(104,"Mahnoor",52,"Dengue",40000,"2025-06-23","2025-06-27")
p5=pateint(105,"Raza",52,"Allergy",2000,"2025-06-23","2025-06-23")

## Calling info function for every object ##
p1.pateint_info()
p2.pateint_info()
p3.pateint_info()
p4.pateint_info()
p5.pateint_info()


## Deleting an object

del p1 
# print(p1) #it will thorugh an error as p1 is deleted
print(p2) # (<__main__.pateint object at 0x00000183CB618CD0>) it will show the object like this as you cannot print an object directly using print().

## Update Object ##

p3.pateint_info()
p3.bill_amount=7000
p3.pateint_info()


