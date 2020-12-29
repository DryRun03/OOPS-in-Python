''' Types of method in Python
  1) Instance Method
      a)Accessors --> To fetch the values 
      b)Mutators --> To modify the values
  2)Class Method
  3)Static Mehtod
  ''' 
#This is Instance Method
class student:
 
    school = "Telusko"    #This is a class variable
    
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
         return(self.m1+self.m2+self.m3)/3
    
    def get_m1(self):      #Accessor Method
        return self.m1

    def set_m1(self,value):    #Mutators Method
        self.m1 =  value
    @classmethod              #Decorator(Class Method)
    def getSchool(cls):           #This is a Class Method
        return cls.school
    @staticmethod             #Decorator(Static Method)
    def info():                   #This is a Static Method
        print("This is student clas.. in ABC Module")

s1= student(34,47,32)
s2= student(45,78,96)

print(s1.avg())
print(student.getSchool())
student.info