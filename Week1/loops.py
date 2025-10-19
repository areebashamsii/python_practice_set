#1.Program to calculate the sum of all even numbers between 1 and 50.

count=0

for i in range(1,51):
    if i % 2 == 0 :
        count+=i

print(count)    

#2.Print all the name in the list using list:

stu_names=["Areeba Shamsi","Rabeea Wasi","Ayesha Malik","Qirat Wajahat"]

for name in stu_names: #The name variable is empty at start but as the loop start It will store each Name one by one in the variable.
    print(name)

#3.program to reverse a string using a loop.(Most Important)

name="Areeba Shamsi"
reverse_name=""

for char in name:
    reverse_name=char+reverse_name
print("Reversed Name:",reverse_name)

#4.Print the maximum number in the tuple:

numbers=(23,45,67,12,90,123,56,78,87,174,89,110)

max_num=numbers[0] #We assume that the first num is the max number because we have to start from 
#somewhere then we will compare this number to find out the max number.
for num in numbers:
    if num > max_num:
        max_num=num
    

print("Maximum Number is:",max_num)

#Program to print factorial using Loop:

num=int(input("Enter a Number to find its factorial:"))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print(f"The factorial of {num} is:",factorial)

# Break and Continue in Loops:

#Break is used when you get the value what you want or a 
#specific condition meet in a loop to increase the loop effiecieny or faster results.

family=["warda","summiya","wahaj","Imran","shazia","areeba","salman","abdulbari"]

input_name=input("Enter Your Name and Check if you are  my family:")

for name in family:
    if name==input_name:
        
      print("Yes! you are a My family.")
      break

#Print names only with 6 letter and skip the rest of the names Using continue Statement:

name_of_empl=["Areeba", "Zain", "Fatima", "Sameer", "Laiba", "Hassan", "Noor", "Tariq", "Amna", "Saniya"]

for name in name_of_empl:
    if len(name) == 4 :
        print(name)
#Taking user input until he exit using while loop:

user_input=input("Type Something or type exit to end")

while True:
    if user_input.lower()=="exit":
        break
print(user_input)


#print number from 1 to 1000
i=0
while i<=1000:
    
    i+=1
print(i)   
    






 