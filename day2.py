#for i in range(50):
 #   print("good morning students")

#i = 1
#while i <=5:
 #   print("good morning students")
  #  i += 1

#def greet():
 #   print("hello students")
  #  print("welcome to python programming  ")
#greet()

#def add(a,b):
 #   result = a + b
  #  print(result)
#add(10, 20)
#add(50, 30)

# students  = ["John", "Alice", "Bob", "Eve"]
# # students.append("Charlie")
# students.remove("Bob")
# print(students)

######tuple#####

# student_details = ("John",  30,  85.5,  True)
# print(student_details)

####dictionaries####

# student = {
#     "name": "John", 
#     "age": 30,
#     "marks": 85.5, 
#     "passed": True
# }
# student ["course"] = "Python Programming"
# student["marks"] = 90.0
# print(student["name"])
# print(student["age"])
# print(student["marks"])
# print(student["course"])

#####class and object####

# class student:
#     def display(self):
#         print("hello students")
#         print("welcome to python programming")
# s1 =  student()
#s1.display()

# class student:
#     def __init__(self):
#         self.__marks = 0\

#     def set_marks(self, marks):
#         self.__marks = marks
#     def show_marks(self):
#         print("student Marks:", self.__marks)
# s1 = student()
# s1.set_marks(85.5)
# s1.show_marks()

#####inheritance##

# class grandfather:
#     def land(self):
#         print("grandfather has a land")

# class father(grandfather):
#     def house(self):
#         print("father has a house")

# class son(father):
#     def car (self):
#         print("son has a car")

# s =  son()
# s.land()
# s.house()
# s.car()

#####polymorphism####

# class animal:
#     def sound(self):
#         print("Animal makes a sound")
# class dog(animal):
#     def sound(self):
#         print("Dog barks")
# class cat(animal):
#     def sound(self):
#         print("Cat meows")
# animals = [dog(), cat(), animal()]                
# for animal in animals:
#     animal.sound()

from abc import ABC, abstractmethod

class payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class upi(payment):
    def pay(self):
        print("Payment done using UPI")
class card(payment):
    def pay(self):
        print("Payment done using Card")
p1 = upi()
p2 = card()
p1.pay()
p2.pay()