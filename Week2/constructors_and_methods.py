## Constructor is a method used to create an instance or an object , it automatically calls whenever the class is called. ##

# def __init__() its a contrcutor method

class product:
     #You can only create one constructor in one class.
    def __init__ (self,product_id="null",product_name="Unknown",price_per_unit="N/A",quantity=0,company="Unknown"): # Dafault parameter of a constructor
        self.product_id=product_id
        self.product_name=product_name
        self.price_per_unit=price_per_unit
        self.quantity=quantity
        self.company=company
    def info(self):
    
        print(f"product_Id:",self.product_id)
        print(f"product_Name:",self.product_name)
        print(f"Price per unit:",self.price_per_unit)
        print(f"Quantity:",self.quantity)
        print(f"Company:",self.company)
        print("\n")


p1=product(1,"Mouse",1200,30,"Logintech")
p2=product()

p1.info()
p2.info() #print p2 with default values.

## Self is not a reserved word or syntac to call an object , you can name it anything.

class vehicle:
     #You can only create one constructor in one class.
    def __init__ (myvehicle,vehicle_id="null",vehicle_name="Unknown",price="N/A"): # Dafault parameter of a constructor
        myvehicle.vehicle_id=vehicle_id
        myvehicle.vehicle_name=vehicle_name
        myvehicle.price=price
    def info(myobject):
        print(f"This is a ",myobject.vehicle_name)

v1=vehicle(201,"Car",200000)
v2=vehicle(202,"Bus",1000000)
v3=vehicle(203,"Aeroplance",30000000)

v1.info()
v2.info()
v3.info()

