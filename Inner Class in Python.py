"""Class inside a class"""
class student:                                   # Outer Class
    def __init__(self,name,rollno):
        self.name= name
        self.rollno= rollno
        self.lap = self.Laptop()                  #This is for taking the value of class Laptop from class student                

    def show    (self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:                                # Inner Class
        def __init__(self):
            self.brand = "Lenovo"
            self.ram = 8
            self.cpu=   "i3"
    
        def show(self):
            print(self.brand, self.cpu, self.ram)

s1=student("Pankaj", 34)
s2= student("Garg",8)

s1.show()                 # For prinitng the value of s1 from class student
# s1.lap.brand            # We have to use it "this way" because laptop is a inner class of a class student   
lap1 = student.Laptop()