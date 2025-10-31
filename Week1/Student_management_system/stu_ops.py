from file_ops import read_data, store_data

def add_stu():
    while True:
        id = input("Enter your Id:")

        if len(id) == 4 and id.isdigit():
            id = int(id)
            break
        else:
            print("You Enter Invalid Id! ID format is : 0008")

    records = read_data(r"C:\Users\USER\Documents\Python\Week1\Student_management_system\records.json")

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
    store_data(r"C:\Users\USER\Documents\Python\Week1\Student_management_system\records.json", records)

    print("Student added successfully!")

add_stu()
