from file_func import read_data ,add_data
from datetime import datetime

class Item():    # This is an item class which has all the attributes or properties of item.
    def __init__(self,item_id,item_name,category,quantity,price_per_unit,supplier,stock_date,expire_date):
        self.item_id=item_id
        self.item_name=item_name
        self.category=category
        self.quantity=quantity
        self.price_per_unit=price_per_unit                 
        self.supplier=supplier
        self.stock_date=stock_date
        self.expire_date=expire_date   # Date is in (yyyy-mm-dd) format

class Inventory():  # This is an inventory class where each item will be stored.
    def __init__(self):  
      self.items=[]
    def add_item(self,item_id,item_name,category,quantity,price_per_unit,supplier,stock_date,expire_date):
        new_item=Item(


            item_id,
            item_name,
            category,
            quantity,
            price_per_unit,
            supplier,
            stock_date,
            expire_date
        )
        self.items.append(new_item)
    def add_item_input():
        print("<<<<<<<<  Add Item in Inventory >>>>>>>")
        
        while True:
            item_id=input("Enter Item Id (000) Format:")
            if item_id.isdigit() and len(item_id)==3:
                item_id=item_id
                break
            else:
                print("Enter Valid Id (000) format!")
                continue

    
        while True:
            item_name=input("Enter Item Name:")
            if item_name!="":
                item_name=item_name
                break
            else:
                print("Name field required!")
                continue
        while True:
            category=input("Choose Item Category:")
            print("1.Food")
            print("2.Clothing")
            print("3.Electronics")
            print("4.Apparels")
            print("5.Furniture")
            print("6.Appliances")
            print("7.Household")
            print("8.School Item")

            if category=="1":
                category="Food"
                break
            elif category=="2":
                category="Clothing"
                break
            elif category=="3":
                category="Electronics"
                break
            elif category=="4":
                category="Apparels"
                break
            elif category=="5":
                category="Furniture"
                break
            elif category=="6":
                category="Appliances"
                break
            elif category=="7":
                category="Household"
                break
            elif category=="8":
                category="School Item"
                break
            else:
                
                print("you Enter Invalid Category!")
                continue
            
        
       
        quantity=input("Enter Quantity:")
        price_per_unit=input("Enter price per unit:")
        supplier=input("Enter Supplier Name:")
        stock_date=datetime.now().strftime("%Y-%m-%d")
        expire_date=input("Enter Item Expire data (yyyy-mm-dd):")
        









