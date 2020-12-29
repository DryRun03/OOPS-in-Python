class Computer:
    def __init__(self):
        self.name= "Pankaj"
        self.age= 21

    def update(self):
        self.age= 30

    def compare(self,other):        
        if self.age == other.age:  
             return True
        else:
            return False         

c1=Computer()
c2=Computer()
c2.age= 28
if c1.compare(c2):
    print("They are Same")
else:
    print("They are Different")

print(c1.name)
print(c2.name)