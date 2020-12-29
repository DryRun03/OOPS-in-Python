class Computer:
    def __init__(self):
        self.name= ("Pankaj")
        self.age= 21

    def update(self):
        self.age= 30

         
c1=Computer()
c2=Computer()

if c1.compare(c2): 
    print("They are Same")


c1.name= "Garg"
c1.age= 20

c1.update()

print(c1.name)
print(c2.name)
print(c1.age)
print(c2.age)
