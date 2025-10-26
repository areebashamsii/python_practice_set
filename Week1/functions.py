## Function syntax ##

def function_name(parameter_s):
    #block of code 
    return #value

## Empty function for code pre_defined Structure ##

def new_func():
    pass

## Simple funtion without parameter: ##

def greet():
    print("Hi, This is Areeba Shamsi!")
greet()

## Python Built_in functions: ##

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

## USER_DEINED Function: ##
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

## Function with Default Parameters: ##
name=input("Enter Your Name:")
score=int(input("Enter your Score:"))

def info(name='None',score=0):
    print(f"Hi {name} ! your score is {score}.")
info(name,score)

##  *args is used when you don't know the axact number of positional arguement: ##

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

## (static) Kwargs ##
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

##  lambda functions ##
#  in python are the one liner function , which doesn't have a name and we directly store the value of function in a variale.
#  we often use when we want simple functions , it's syntax is simple than
# the ordinary function , can be used inside a loop or statement,it returns it values on its own


#sum 3 number by using Lambda function 
#Syntax:
# variable_name=lambda parameters : statement 
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
z=int(input("Enter third number:"))

sum=lambda x,y,z: x+y+z
print(sum(x,y,z))

#sqaure:

sum=lambda x: x*x
print(sum(x))


## map() ## 
# is the function used to perform same task for each element.syntax: map(func,iterable varible )
#list() will store each iterable element of celcius list into a farenhite list after results
celcius=[23,45,12,0,17]
farenhite=list(map(lambda c:9/5*c+32,celcius)) #c is item in celcius
print(farenhite)

#print even numbers and odd numbers seperately from the list using lambda function:
## filter() ## 
# function only stores value after certain condition becomes true , it filters out data on a condition:

list_num=[23,45,32,68,33,76,13,98,27]

even_num=list(filter(lambda n:n % 2==0,list_num))
print(even_num)
odd_num=list(filter(lambda n:n % 2!=0,list_num))
print(odd_num)

## Sort student based on their score using lambda function and sorted() function: ##

stud_info=[("Ali",86),("zainab",84),("Areeba",98),("fatima",77)]

sort_by_score=sorted(stud_info, key=lambda x: x[1] ,reverse=True)
print(sort_by_score)

#Important point: we use list() func in 1st and 2nd program but not in 3rd because filter() and map() iterate in list one by one
#where as sorted() immediately created a new sorted list.

## Nested Function ##
#function within a function is called nested function:

#add float values and print its absolute value by round off.
val_1=float(input(("Enter float value 1 to add:")))
val_2=float(input(("Enter float value 2 to add:")))
def round_float():
    def add_float():
      return val_1+val_2
    result=add_float()
    return round(result,0)

print(round_float())

## Recursive Function ##
#print given number's factorial using recursive function

#function calling itself is recursive function

num=int(input("Enter number to find its factorial:"))

def factorial(num):
    if num==1 or num==0:
        return 1
    else :
        return num*factorial(num-1)
print(factorial(num))  

## Higher Order Functions ##

## map() ## 
# is the function used to perform same task for each element.syntax: map(func,iterable varible )
#list() will store each iterable element of celcius list into a farenhite list after results
celcius=[23,45,12,0,17]
farenhite=list(map(lambda c:9/5*c+32,celcius)) #c is item in celcius
print(farenhite)

#print even numbers and odd numbers seperately from the list using lambda function:
## filter() ## 
# function only stores value after certain condition becomes true , it filters out data on a condition:

list_num=[23,45,32,68,33,76,13,98,27]

even_num=list(filter(lambda n:n % 2==0,list_num))
print(even_num)
odd_num=list(filter(lambda n:n % 2!=0,list_num))
print(odd_num)

## Sort student based on their score using lambda function and sorted() function: ##

stud_info=[("Ali",86),("zainab",84),("Areeba",98),("fatima",77)]

sort_by_score=sorted(stud_info, key=lambda x: x[1] ,reverse=True)
print(sort_by_score)

#Important point: we use list() func in 1st and 2nd program but not in 3rd because filter() and map() iterate in list one by one
#where as sorted() immediately created a new sorted list.


import functools  #import the module "functool" to use reduce func

#print max number using reduce()

numbers=input("Enter Numbers to find the MAX num:") #It will take values from user and create a list 
number_list=list(map(int,numbers.split()))

max_num=functools.reduce(lambda x,y:x if x>y else y,number_list)

# reduce() only retrun one value from the list , by adding all , multiplying all 
#finding min or max but only one output
#it wil compare the first two element then repeat the process until the end.

print(max_num)

## Docstring , it returns the string or triple quoted comment from the fucntion which tells what the function do ##
    
a=5
b=8
def add(a,b):
    """ It returns the sum of 'a' and 'b' """
    return a+b
print(add(a,b))
print(add.__doc__) #print the comment inside the func

## Type hinting ##

x=input("Enter numers to find the maximum one:")
num_list=list(map(int,x.split()))

def find_max(num_list)->int:
     return max(num_list)  #It predicts what the function will return an int , a string , a list or what.
#Type hinting helps prevent errors by showing warnings when wrong data types are used, and 
# it makes debugging easier by clearly showing what type of input or output a function expects.
   
print(find_max(num_list))
    
## Decorators ##
def greet_decorator(func):
   def wrapper(*args, **kwargs):
    
    print("Guess the Number right to win!")

    func(*args, **kwargs)
    print("Thank you so much for playing!")
   return wrapper


# guess the number 
z=int(input("Enter a number to guess:"))
@greet_decorator #attach this fucntion with timer decorator function
def guess_num(z):
    if z==16:
        print("Congratulations! you guessed the right Number")
    else:
        print("Sorry! you guessed the wrong number,Try again.")
guess_num(z)