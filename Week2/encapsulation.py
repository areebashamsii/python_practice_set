
## Encapsulaion : Creating a private property or attribute
class Students:
        def __init__ (self,name,id,class_no,fee=0):
                self.name=name 
                self.id=id 
                self.class_no=class_no
                self.__fee=fee
        def print_stu_info(self):
                print("Name:",self.name)
                print("Id:",self.id)
                print("Class no::",self.class_no)
                # print("Fee:",self.fee)  

s1=Students("Areeba",8,14,100000)  # 100000 fee will not print because it is a private attribute
s1.print_stu_info()

## Access the private variable using the getter method

class Students_info:
        def __init__ (self,name,id,class_no,fee=0):
                self.name=name 
                self.id=id 
                self.class_no=class_no
                self.__fee=fee
        def get_fee(self):
                return self.__fee   # This is a getter method used to access private attribute
        def print_stu_info(self):
                print("Name:",self.name)
                print("Id:",self.id)
                print("Class no::",self.class_no)
                print("Fee:",self.get_fee())  

s1=Students_info("Areeba",8,14,1000) 
s1=Students_info("Areeba shamsi",8,14,20000)  # It assign new value to s1 by overwriting previous s1

s1.print_stu_info()   

## change the private variable using the setter method

class user:
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.__password=password
    def get_password(self):
           return self.__password
    def set_password(self,new_password):
           self.__password=new_password

    def print_user_info(self):
                print("Name:",self.name)
                print("Email:",self.email)
                print("Password:",self.get_password())

user1=user("Areeba Shamsi","areebashamsi1015@gmail.com",12345)          
user1=user("Areeba Shamsi","areebashamsi1015@gmail.com",1000) #Redeclarion complete change the object not only passwrd ,it creates a new object and remove old values
user1.print_user_info()
user1.set_password(54321)    #change the password using setter method safely without making changes in otehr attribute
user1.print_user_info()

## Property DEcorators: ( it chnages the method into property so that we can identifies getter and seter method as attribute variable)

class Customer:
        def __init__(self,name,total_bill,transaction_id):
                self.name=name
                self.__total_bill=total_bill
                self.__transaction_id=transaction_id
        @property
        def total_bill(self):
                return self.__total_bill
        @total_bill.setter
        def total_bill(self,new_total_bill):
                self.__total_bill=new_total_bill
        @property
        def transaction_id(self):
                return self.__transaction_id
        @transaction_id.setter
        def transaction_id(self,new_transaction_id):
                self.__transaction_id=new_transaction_id

        def print_customer_info(self):
                print("Name:",self.name)
                print("Total Bill:",self.total_bill)  # now we can use getter and setter method as a property or variable
                print("Transaction:",self.transaction_id) 


c1=Customer("Areeba Shamsi",7000,112233)
c1.print_customer_info()
c1.transaction_id=998877   # Use a method as variable or a property
c1.print_customer_info()

## Protected Attribute:

class patient:
       def __init__(self,name,pateint_id,disease):
            self.name=name                                            #Attributes prefixed with a single underscore _ are protected.
            self.pateint_id=pateint_id                                        #Accessible but should not be touched directly; subclasses can use them. 
            self._disease=disease                                      # ( it is mainly used to warn developers that do not make changes in this directly)

       def print_pateint_info(self):
                print("Name:",self.name)
                print("Pateint ID:",self.pateint_id)  # now we can use getter and setter method as a property or variable
                print("Disease:",self._disease)
 
p1=patient("Tehreem",123,"High Blood pressure")
p1.print_pateint_info()
