#Create Variable:
num=None
str_val=None
boole=None

#Declare a Variable:

#Storing Values in Variable:

type_num=15 #Store an int
type_float=12.34 #Store a float
type_str="Areeba Shamsi" #Store a String
type_boolean=True #Storing a Boolean Value

#Python variable can hold many data types:

#Immutable Data Types:
age=22
ratio=5.6
name="Areeba Shamsi"
is_adult=True
marks=(76,45,35,89) #This is a Tuple (Ordered)
balance=None #This is initialized Variable and it has null value(Ordered)

#Mutable Data Types:
cars=['Corvette',"Porche","Dodge RAM","Mustang",32,45,25] #This is a List
stu_ids={111,122,133,144,122,133,155} #This is the set (Unordered), automatically remove duplicate Value 
post_info={

    "Areeba Shamsi":"CEO",
    "Fatima Zehra":"Manager",
    "Ali Rehman":"Technician",
    "Asad Mirza":"Employee"

}

#Print all Variables:
print(age)
print(name)
print(ratio)
print(is_adult)
print(marks)
print(balance)
print(cars)
print(post_info)
print(stu_ids)

#Data Type Checking

print(type(age))
print(type(name))
print(type(ratio))
print(type(is_adult))
print(type(marks))
print(type(balance))
print(type(cars))
print(type(post_info))
print(type(stu_ids))

#Multiple Assignments:

_age,_name,_full_name=22,"Areeba","Shamsi"
print(_age,_name,_full_name)

#Assigning Same Value to Multiple Variable:
a = b = c = d=5
print(a,b,c,d)

#Conversion of Data Type:

x=24
x=str(x)
print(type(x))
y='24'
y=int(y)
print(type(y))

#Scope of Variable:
#Local Scope Variable

#Varible declare inside a fucntion is local scoped Variable , cannot be accessed outside the function.

def info():
    my_name="Areeba Shamsi"
    my_age=22
    is_studying=True
    print(my_name,my_age,is_studying)

# print(my_name)               through a "not defined" Error
info()                        #If This function will be called then the variable will be accessable.


#Converting Local Scope Variable into Global Scope Variable.

def info2():
    global  my_name2, my_age2, is_studying2  #Global keyword will convert Local Variable into Global Variable
    my_name2="Areeba Imran Shamsi"
    my_age2=22
    is_studying2=True
info2()
print(my_name2,my_age2,is_studying2)
   
   
   

#Gobal Scope Variable:
#Variable outside the function will be accessable any where in the code , that is called Global Scoped.

stu_name="Areeba Shamsi"
stu_marks=95
stu_grade="A+"

def stu_info():
    print(stu_name,stu_marks,stu_grade)

stu_info() #These outside declared variable will be accessable inside and outside the function.

#Delete variable

uni_name="SMIU"
location="II Chundrigar Road"
print(uni_name,location)

del uni_name
# print(uni_name,location)             #This Will through an error "uni_name not defined"