class Student:
     def __init__(self,name,regno,age,grade):
         self.name=name
         self.regno=regno
         self.age=age
         self.grade=grade

     def is_honour(self):
         if self.grade=="a":
             print(f"{self.name} is a honour student")
         elif self.grade=="b":
             print(f"{self.name} is not a honour student")
         else:
             print("invalid")
             
         
         



