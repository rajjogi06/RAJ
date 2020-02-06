class student:
    def __init__(self,name,rollno,DM,WP,OOPs):
        self.name=name
        self.rollno=rollno
        self.DM=DM
        self.WP=WP
        self.OOPs=OOPs

    def display(self):
        
        print("name: ",self.name)
        print("rollno: ",self.rollno)
        print("marks of DM: ",self.DM)
        print("marks of WP: ",self.WP)
        print("marks of OOPs: ",self.OOPs)

    def final_result(self,DM,WP,OOPs):
        self.tot=DM+WP+OOPs
        self.res=100*(self.tot/300)
        print("total marks is: ",self.tot)
        print("total percent is: ",self.res)
        if(self.res>=75):
            print("the grade obtain is:A")
        elif(self.res>=50):
            print("the grade obtain is:B")
        elif(self.res>=75):
            print("the grade obtain is:C")
        else:
            print("the grade obtain is:F")
            
            
            


    

name=input("plz enter your name: ")
rollno=int(input("plz enter your roll no.: "))
DM=float(input("plz enter your marks of DM.: "))
WP=float(input("plz enter your marks of WP.: "))
OOPs=float(input("plz enter your marks of OOPs.: "))


s1=student(name,rollno,DM,WP,OOPs)
s1.display()
s1.final_result(DM,WP,OOPs)     
