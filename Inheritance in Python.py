"""Child Node/Parent Node"""

class A:                                        #Parent Class of B and a Grandparent of C
    def feature1(self):
        print("Feature 1 Working")

    def feature2(self):
        print("Feature 2 Working")

class B(A):                                     #Child Class of A and a parent of class C
    def feature3(self):
        print("Feature 3 Working")

    def feature4(self):
        print("Feature 4 Working")


class C(B):                                    #Child class of class B
    def feature5(self):
        print("Feature 5 Working")

a1= A()
a1.feature1()
a1.feature2()

b1= B()
b1.feature1()
b1.feature2()