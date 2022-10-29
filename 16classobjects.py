# class mohit:


#     def __init__(self,id,name,salary):
#         self.id=id
#         self.name=name
#         self.salary=salary

#     def input(self):
#         self.id=input("Enter your id :")
#         self.name=input("Enter your Name :")
#         self.salary=input("Enter your salary :")
    
#     def __str__(self):
#         print(f"The employess id no is {self.id} and its name is {self.name} and salary is {self.salary}")

#     # def info(self):
#     #     print(self.id,self.name,self.per)
    
   

# p1=mohit(0,0,0)
# p1.input()
# p1.__str__()


# inheritance

# class base:
#     def __init__(self,id,name):
#         self.id=id
#         self.name=name

#     def input(self):
#         self.id=input()
#         self.name=input()

# class derived(base):

#     def __init__(self,salary,id,name):
#         super().__init__(id,name)
#         self.salary=salary 

#     def input(self):
#         super().input(self.id,self.name)
#         self.salary=input()

#     def info(self):
#         print(self.id,self.name,self.salary)


# d1=derived(0,0,0)
# d1.input()
# d1.info()


# class base:
#     def __init__(self,id,name):
#         self.id=id
#         self.name=name

#     def input(self):
#         self.id=input()
#         self.name=input()

# class derived(base):

#     def __init__(self,salary,id,name):
#         super().__init__(id,name)
#         self.salary=salary 

#     def input(self):
#         self.id=input("Enter your id :")
#         self.name=input("Enter your name :")
#         self.salary=input("Enter your salary :")
        
#     def info(self):
#         print(self.id,self.name,self.salary)


# d1=derived(0,0,0)
# d1.input()
# d1.info()


#destructor

class A:
    def __init__(self):
        print("Constructor called")
    def __del__(self):
        print("Destrctor called")
    
p1=A()
del p1