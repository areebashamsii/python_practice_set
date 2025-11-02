from file_ops import read_data, store_data
import os
import json
filename=r"C:\Users\USER\Documents\Python\Week1\Student_management_system\records.json"

def add_stu():
    print("Add Student in record.")
    records = read_data(filename)
    while True:
        id = input("Enter your Id:")

        if len(id) == 4 and id.isdigit():
            
            break
        else:
            print("You Enter Invalid Id! ID format is : 0008")

   

    for student in records:
        if student['Id'] == id:
            print("This ID already exists! Add new ID:")
            add_stu()
            return

    name = input("Enter your Name:")
    age = input("Enter your Age:")
    department = input("Enter your Department:")

    stu_info = {
        "Id": id,
        "Name": name,
        "Age": age,
        "Department": department
    }

    records.append(stu_info)
    store_data(filename, records)

    print("Student added successfully!")

def update_stu():
    print("Update Student record.")
    records = read_data(filename)
    update_id=input("Enter Student Id to update your record:")
    
    for student in records:
        
        if student["Id"] == update_id:
                
           update_name=input("Enter New Name:")
           update_age=input("Enter New Age:")
           update_department=input("Enter New Department:") 

           student["Id"]=update_id
           student["Name"]=update_name
           student["Age"]=update_age
           student["Department"]=update_department
            
           store_data(filename, records)

           print("Record updated successfully!")
           break
    else:
        print("This Id does not exist!")
        update_stu()

def delete_stu():
    print("Delete Student from record.")
    records = read_data(filename)
    del_id=input("Enter Student Id to delete the record:")
    
    for student in records:
        
        if student["Id"] == del_id:
            confrm=input("Are you Sure to delete your record? (Yes or No)")
            
            if confrm.lower()=="yes":
                   
                   records.remove(student)
                   store_data(filename, records)
                   print("Record Deleted Successfully!")

            else:
                print("Invalid Input! Enter yes or No")
            break
         
                
            
    else:
     print("This Id does not Exist!")

def check_records():
   records=read_data(filename)
   if records==[]:
       print("No record has been stored!")
       print("Add student")
       add_stu()
   else:
        
        print("-----STUDENTS RECORDS-----")
        for student in records:
           print(f"ID:{student["Id"]}")
           print(f"Name:{student["Name"]}")
           print(f"Age:{student["Age"]}")
           print(f"Department:{student["Department"]}")
           print("\n")
        




