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