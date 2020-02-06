class Employee(object):
     def __init__(self):
          C_N=str(input("ENTER THE COMPANY NAME= "))
          C_A=str(input("ENTER THE COMAPNY ADDRESS= "))
          E_ID=str(input("ENTER THE EMPLOYEE ID= "))
          E_N=str(input("ENTER THE EMPLOYEE NAME= "))
          E_Q=str(input("ENTER THE EMPLOYEE QUALIFICATION= "))
          

class Salary(object):
     def __init__(self):
          E_BS=int(input("ENTER THE BASIC SALARY= "))
          TA=(18*E_BS)/100
          DA=(17*E_BS)/100
          HRA=(25*E_BS)/100
          EPF=(10*E_BS)/100
          total=TA+DA

class Net_Salary(Employee,Salary):
     def __init__(self):
          Employee.__init__(self)
          Salary.__init__(self)
          print("Net_Salary")

     def SAL(self):
          print("total")

ob = Net_Salary()
ob.SAL()
