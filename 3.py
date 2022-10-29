# slicing datatype[start : stoping:[stepsize=1]]
# myname="mohit sharma"
# print(myname[0:5])
# print(myname[0:5:2])

# function-------
# def greeting():
#     print("Hey users")

# def greeting(username):
#     print("Hey users",username)

# def greeting(username):
#     print(f"Hey users {username} welcome in Tech")

# # greeting()
# greeting("mohit")

# swapping----
# a=10
# b=20
# a,b=b,a
# print(a)

# age=10
# print(id(age))
# salary=10
# print(id(salary))

# def listupdate(listmult):
#     print(listmult)

# mylist=[10,20,30]
# print("before func",mylist)
# listupdate(mylist)
# print("before func",mylist)

# def listupdate(listmult):
#     for value in range(0,len(mylist)):
#         listmult[value]=listmult[value]*2

  

# mylist=[10,20,30]
# print("before func",mylist)
# listupdate(mylist)
# print("before func",mylist)

# from email.policy import default


# def employeeDetail(eid,ename,salary=1100):
#     print(f"hey eid {eid},ename is {ename},salary is {salary}")

# employeeDetail(100,"mohit",5)   #postion argument
# employeeDetail(salary=100,ename="mohit",eid=5)  key word aregument
# employeeDetail(5,salary=100,ename="mohit") postion and key word argumet
# employeeDetail(5,ename="mohit") default argument
# def employeeDetails(*details):   # variable length argument
#     print(type(details))
#     print(details)    

# # employeeDetails(10,'hey user',"cakecuting")
# employeeDetails()    why is running its assignment


# keyword variable length argument
# variable length argument*args   keywordl variable length argument**kwargs 
# def employeeDetails(**details):   
#     print(type(details))
#     print(details)    

# employeeDetails(username=0)

# first class function and high order function

# def message():
#     print("Did you see me")

# output = message
# a=output()
# print(a)

# lambda : oneline Function
# lambda arg1,arg2 :Expression

# out=lambda x : x*2
# print(out(10))

# map,filter,reduce

# def addnumber(num1):
#     return num1+1


# # out=addnumber(19)
# # print(out)
# a=list(map(addnumber,[10,20,30]) )
# print(a)

# class is a blue print and template
# characterstics (variable)
# functionality(function)
# john object(instance)

# class and objects====

# class person:
#     id=101
#     s_name="Mohit"

# p1=person()
# print(p1.id,p1.s_name)

# class person:
#     id=101
#     s_name="Mohit"

#     def info(self):
#          self.id,self.s_name

# p1=person()
# print(type(p1.info()))
# print(p1.info())


# class person:
#     def __init__(self,id,name):
#         self.s_id=id
#         self.s_name=name
 

#     def info(self):
#          print(self.s_id,self.s_name)

# p1=person(10,"mohit")
# print(p1.info())


# eid ename esalary

# class employee:

#     company="REGex"      #class variable

#     def __init__(self,id,name,salary,email):
#         self.eid=id                                        #instance variable
#         self.ename=name                                   
#         self.salary=salary
#         self.email=email

#     def info(self):
#         print(self.eid,self.ename,self.salary,self.email)

# p1=employee(10,"mohit",1000,"mohit@gmail.com")
# p1.info()



# class student:
#     count=0
#     def __init__(self):
#         self.count=student.count+1
        
# s1=student()
# print(s1.count)

# s2=student()
# print(s2.count)


# class student:
#     count=0
#     def __init__(self):
#         student.count=student.count+1
        
# s1=student()
# print(s1.count)

# s2=student()
# print(s2.count)

# class Driver:
#      def __init__(self,id,name,salary,email,wallet):
#         self.eid=id                                       
#         self.ename=name                                   
#         self.salary=salary
#         self.email=email
#         self.wallet=wallet

#      def info(self):

#         print(self.eid,self.ename,self.salary,self.email,self.wallet)
    
# class customer(Driver):
#      def __init__(self,id,name,salary,email,wallet,status):
#         super().__init__(id,name,salary,email,wallet)
#         self.status=status
  

#      def info(self):

#         print(self.eid,self.ename,self.salary,self.email,self.wallet,self.status)

# mohit=customer(10,"Mohit",1000,"mohit@gmail.com",50000,"ridding")
# print(mohit.info())

# class Tatamoters:
#     _amount=10

# class Harrier(Tatamoters):
#     year=2022

# h1=Harrier()
# print(h1._amount)


# class Tatamoters:
#     _amount=10

# class Harrier(Tatamoters):
#     year=2022

# t1=Tatamoters()
# print(dir(t1))

# h1=Harrier()
# print(h1._amount)


# os
# import os
# pyautogui
# selenium
# matplotlib,seaborn,
# Datascienc,numpy,pandas,scikitlearn,tensorflow,scipy