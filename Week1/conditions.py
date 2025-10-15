#Conditions in python used for making desicions:

#Basic Structure of condition or desicion Tree

num=int(input("Enter Number to check if it is even or odd:"))

if num%2 == 0:
  print("This is an even number.")
elif num%2 != 0:
  print("This is an odd number.")
else:
  print("you enter an invalid number!")

 #Check Which number is the biggest among 3:  

num1=int(input("Enter a number 'a' for comparison :"))
num2=int(input("Enter a number 'b' for comparison :"))
num3=int(input("Enter a number 'c' for comparison :"))

if num1 > num2 and num1 > num3 :
  print("Number a is the biggest")
elif num2 > num1 and num2 > num3 :
  print("Number b is the biggest")
elif num3 > num1 and num3 > num2 :
  print("Number c is the biggest")
else:
  print("You enter the same number")

#Login authentication:

login_info=input("Enter email or user_name:")
password=int(input("Enter your password:"))

if login_info == "Areeba Shamsi" or login_info == "areebashamsi1015@gmail.com" and password ==1234:
  print("Access Granted!")
else:
  print("Access Denied!")

#Ternary Operator use
#one line or single line Condition
age=int(input("Enter your age to check if you are eligable or not:"))
print("You are eligable!") if age>=20 and age<=30 else print("You are not eligiable!")