class computer:
    def __init__(self,id,name):
        self.id_=id
        self.name_=name
    def config(self):
        print("hhisdjs", self.id_,self.name_)

comp1=computer('i5','lenovo')
comp2=computer('i7','apple')


comp1.config() #object creation 
comp2.config()

# constructor, initializing variables in __init__
class constructor:
    def __init__(self) -> None:
        self.age=25
        self.name='kavya'
    def compare(self,other):
        print("other",other.age)
        if self.age==other.age:
            return True
        else:
            return False

c1=constructor()
c1.age=30
c2=constructor()
c2.age=40

#c1.name='paul'
if c1.compare(c2):
    print("They are same")
else:
    print("they are different")

# print(c1.name)
# print(c2.name)

#variables in oops (instance variable, class(static varaibles))

class car:
    wheels=4 # class variable 
    def __init__(self) -> None:
        self.mil=10 #instance
        self.com='BMW' #instance variable

c1=car()
c2=car()
c1.mil=20

car.wheels=7  # value shared among all other obj 
print(c1.mil,c1.com,c1.wheels)
print(c2.mil,c2.com, c2.wheels)

# Typed of method  1) Instance methods 2) class Methods 3) Static methods 

class student:
    school='telusko' #class variables 
    def __init__(self,m1,m2,m3) -> None:
        self.marks1=m1 #instance variables 
        self.marks2=m2
        self.marks3=m3
    def avg(self): #instance method
        return (self.marks1+self.marks2+self.marks3)/3
    @classmethod
    def getschool(cls):
        return cls.school

s1=student(12,12,12)
s2=student(12,34,56)

print("avgggggg",s1.avg()) #instance method calling
print("avgggggg",s2.avg())

print(student.getschool()) #class method caling

#Inner class
class outer: #outer class

    def __init__(self,name,roll) -> None:
        self.name=name
        self.roll=roll
        self.lap=self.inner() #object creation of inner class
    
    def show(self):
        print(self.name,self.roll)
        self.lap.show()
    
    #inner class
    class inner:

        def __init__(self) -> None:
            self.brand='HP' 
            self.cpu='i5' 
        def show(self):
            print (self.brand,self.cpu)

s1=outer('kavya',20)  #s1 = constructor of outer
s2=outer('paul',29)

s1.show()
s2.show()

lap1=s1.lap #object for inner class variables 
lap2=s2.lap



print("inner obi creation inside outer class",lap1.brand) # calling inner class 
#print("inner claas",s1.lap.brandbrand)
#print("s1",s1.name,s1.roll)

lap3=outer.inner()
print("inner obj creation outside of outer class",lap3.brand)

#inheritance
class A:
    def feature1(self):
        print("feature1")
    def feature2(self):
        print("feature2")

class B(): #class B(A) single level 
    def feature3(self):
        print("feature3")
    def feature4(Self):
        print("feature4")

class C(A,B): #class C(B) multilevel, class C(A,B) multiple inh
    def feature5(self):
        print("feature5")
a1=A()
b1=B()
c1=C()

a1.feature1()
a1.feature2()

b1.feature3()

#How constructor works in inheritance , method resolution oreder

class A_inh:
    def __init__(self) -> None:
        print("In A in Init")
    def feature1(self):
        print("feature1 in A")
    def feature3(self):
        print("feature222222 -3333 in A")


class B_inh(): #class B(A) single level
    def __init__(self) -> None:
        #super().__init__() #super represnts the super class init
        print(" B init") 
    def feature1(self):
        print("feature 1 in B")
    def feature2(self):
        print("feature222222 in B")
    # def feature3(self):
    #     print("feature33333 in B")

#class C(B) multilevel, class C(A,B) multiple inh
class C_inh(A_inh,B_inh):
    def __init__(self) -> None:
        super().__init__()
        print("in C init")
    
    def feat(self):
        super().feature3()



#a1= A_con()
#b1=B_con()
c1= C_inh()
c1.feature1()
c1.feat()

#operator overloadig

a="5"
b="9"
#int => class lo __add__ aneydhi method
#print(int.__add__(a,b))
print(str.__add__(a,b))

class Stu:
    def __init__(self,m1,m2) -> None:
        self.m1=m1 
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=Stu(m1,m2)
        return s3
    def __gt__(self,other):
        s1= self.m1+self.m2
        s2=other.m1+other.m2
        if s1>s2:
            return True
        else: return False


s1=Stu(1,21)
s2=Stu(43,23)

s3=s1+s2

print(s3.m2)

if s1>s2:
    print("s1 wins")
else:print("s2 win")

# method overloading is not supported in python 
#method overriding

class Apple:
    def show(self):
        print("I am parent")
class Banana(Apple):
    def show(self):
        print(" Ia m in class show")

A=Apple()
B=Banana()

A.show()
B.show()

