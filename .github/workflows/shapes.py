class shapes:
    def __init__(self,l,b,area_rectangle,area_square,perimeter_rectangle,perimeter_square):
        self.l=l
        self.b=b
        self.area_square=square
        self.area_rectangle=rectangle
        self.perimeter_square=square
        self.perimeter_rectangle=rectangle

def area_square(self,l):
    A=self.l*self.l
    return A

def perimeter_square(self,l):
    B=self.l*4
    return B

def area_rectangle(self,l,b):
    c=self.l*self.b
    return c

def perimeter_rectangle(self,l,b):
    D=2(self.l+self.b)
    return D

l = int(input("Enter the number="))
b = int(input("Enter the number="))
S1 = shapes(l,b)

print("select shape = ")
print("1.square")
print("2.rectangle")

choice = input("Enter the choice= ")

if choice==square:
    print("the area of square is = ",S1.area_square(l))
if choice==square:
    print("the area of square is = ",S1.perimeter_square(l))
if choice==rectangle:
    print("the area of rectangle is = ",S1.area_rectangle(l,b))
if choice==rectangle:
    print("the perimeter of rectangle is = ",S1.perimeter_rectangle(l,b))







    
