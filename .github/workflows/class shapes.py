class shapes:
    def square(self,s):
        self.side=s

    def rectangle(self,l,b):
        self.length=l
        self.breadth=b

    def calculate(self):
        self.periofasquare=4*s
        self.periofarect=2*l+2*b
        self.areaofasquare=s*s
        self.areaofarect=l*b

    def display(self):
        print("\nPerimeter of a square = ",self.periofasquare)
        print("Perimeter of a rectangle = ",self.periofarect)
        print("Area of a square = ",self.areaofasquare)
        print("Area of a rectangle = ",self.areaofarect)
        
s1=shapes()
s=int(input("Enter a side of a square : "))
l=int(input("Enter a length of a rectangle : "))
b=int(input("Enter a breadth of a rectangle : "))
s1.square(s)
s1.rectangle(l,b)
s1.calculate()
s1.display()


        
    
