class Employee(object):
     def __init__(self):
          C_N=int(str("ENTER THE COMPANY NAME= "))
          C_A=int(str("ENTER THE COMAPNY ADDRESS= "))
          E_ID=int(input("ENTER THE EMPLOYEE ID= "))
          E_N=int(str("ENTER THE EMPLOYEE NAME= "))
          E_Q=int(str("ENTER THE EMPLOYEE QUALIFICATION= "))
          E_BS=int(str("ENTER THE BASIC SALARY= "))

class Salary(object):
     def __init__(self):
          TA=(18*E_BS)/100
          DA=(17*E_BS)/100
          HRA=(25*E_BS)/100
          EPF=(10*E_BS)/100

class Net_Salary(Employee,Salary):
     def __init__(self):
          Employee.__init__(self)
          Salary.__init__(self)
          print("Net_Salary")

     def SAL(self):
          print(E_BS+TA+DA+HRA-EPF)

ob = Net_Salary()
ob.SAL()
