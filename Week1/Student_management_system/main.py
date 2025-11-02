from stu_ops import add_stu,update_stu,delete_stu,check_records

print("-----welcome to Student Management System!-----")
def menu():
    print("1. Add New Student.")
    print("2. Update Student record.")
    print("3. Delete Student from the record.")
    print("4. Check Records.")
    print("5. Exit")


    option=input("Enter Option number from above to proceed:")

    if option =="1":
      add_stu()
      next_step()

    elif option =="2":
      update_stu()
      next_step()
    elif option =="3":
      delete_stu()
      next_step()
    elif option =="4":
      check_records()
      next_step()
    elif option =="5":
   
     print("Thank you so much for Visiting our App!")

    else:
     print("This Option does not exist,Enter Again:")
     print("\n")
     menu()
     

def next_step():
    d=input("Enter ""M"" for Menu or Enter ""E"" for Exit:")
    if d.lower()=="m":
        menu()
    elif d.lower()=="e":
       print("Thank you so much for using our App!")
    else:
       print("You enter invalid input")


menu()