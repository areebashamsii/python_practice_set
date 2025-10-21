#Function syntax

def function_name(parameter_s):
    #block of code 
    return #value

#Empty function for code pre_defined Structure:

def new_func():
    pass

#Simple funtion without parameter:

def greet():
    print("Hi, This is Areeba Shamsi!")
greet()

#python Built_in functions:

my_list=[12,34,67,43,35,246,2446,89]
my_name="Areeba Shamsi"

#len(variable_name)
print(len(my_name))
print(len(my_list))

# sum(variable_name)
print(sum(my_list))

#max(variable_name)
print(max(my_list))
#min(variable_name)
print(min(my_list))

#sorted(variable_name)
print(sorted(my_list))

#USER_DEINED Function:
#Take an input of number and print its square:

num=int(input("Enter a Number to find its square:"))

def square(num):
    num=num*num
    return num
print(square(num))

# Convert km into m:

dis_in_km=int(input("Enter distance in Km to Convert m :"))

def km_to_m(dis_in_km):
    global dis_in_m
    dis_in_m=dis_in_km*1000
    return dis_in_m
print(km_to_m(dis_in_km))

# Function with Default Parameters:
name=input("Enter Your Name:")
score=int(input("Enter your Score:"))

def info(name='None',score=0):
    print(f"Hi {name} ! your score is {score}.")
info(name,score)

#  *args is used when you don't know the axact number of positional arguement:

numbs=input("Enter as many number for its sum (seperate numbers with space):",)
num_list=[int(x) for x in numbs.split()]  #numbs.split will split the above spaced number in each number and will create a list.

def add(*num_list): # *variable_name will work as a parameter whose value is not defined until user stops.
    total=0
    for num in num_list:
        total+=num
    return total
print(add(*num_list))

# Enter no of students score to find the average using *args

score=input("Enter Students score and seperate each score with a space:")
all_score=[int(x) for x in score.split()]

def avrg(*all_score):
    total=0
    for x in all_score:
        total+=x
    return total/len(all_score)
print(avrg(*all_score))

# (static) Kwargs
def info(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")

print(info(pakistan="karachi",china="bejing",russia="Moscow",india="Delhi"))

# (Dynamic) **kwargs is used for no of keywords arguments , like it will create a dictionary when you don't know the no of items.

name=input("Enter Your Name:")
age=int(input("Enter Your age:"))
country=input("Enter Your country Name:")

def info(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")

print(info(name=name,age=age,country=country))



