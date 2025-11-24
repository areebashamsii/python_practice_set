
## Single Level Inheritence

class Faculty:
    def job(self):
        print("Teach Student")
class Software_teacher(Faculty):
     pass
f1=Software_teacher()
f1.job()

## Multiple Inheritence
class price:
    def price(self):
        print("The price of this product is pkr 900.")
class quantity:
    def quantity(self):
        print("The quantity of the product is very less")   
class product(price,quantity):   #Product class inherit functions of both classes.
    pass

p1=product()
p1.price()
p1.quantity()

## multi-level inheritence

class Employee:
    def work(self):
        print("Employee do the work.")
class Manager(Employee):
    def manage(self):
        print("Manager Manage the Work.")
class Director(Manager):                              #Director inherit the work function from manager class as manager class inherit the function of employee class.
    def plan(self):
        print("Director Plan the work.")

e1=Director()
e1.plan()
e1.manage()
e1.work()

## Hybrid Inheritence ( Any two types of class work together make a hybrid class


# Single inheritence
class Monitor:
    def monitor(self):
        print("I am a Monitor")
class Student(Monitor):            
    def student(self):
        print("I am a Student.")

# Multi-level Inheritence
class Daughter(Student):
    def daughter(self):
        print("I am a Daughter.")
class Employee(Daughter):
    def employee(self):
        print("I am an Employee.")

# Hybrid Inheritence
class person(Employee):
    def person(self):
        print("I am a person.")

p1=person()
p1.student()
p1.person()
p1.daughter()
p1.monitor()
p1.employee()


## super() (It is a function used to call the method of parent class in child class)


class Person:
    def person(self):
        print("I am a person.")
class Employee(Person):
    def employee(self):
        super().person()
        print("I am an Employee.")

e1=Employee()
e1.employee()
