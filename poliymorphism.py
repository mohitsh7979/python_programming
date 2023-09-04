# print(len("mohit"))
# print(len("mohit"))

# Poliymorphism With Class Methods

# class A():
#      def __init__(self,name,father_Name):
#         self.name=name
#         self.father=father_Name
#      def input(self):
#         self.name=input("Enter your Name :")
#         self.father=input("Enter your Father Name :")
#      def info(self):
#         print(self.name,self.father)
        




# class b():
#      def __init__(self,name,father_Name):
#         self.name=name
#         self.father=father_Name
#      def input(self):
#         self.name=input("Enter your Name :")
#         self.father=input("Enter your Father Name :")
#      def info(self):
#         print(self.name,self.father)


# obj_a=A(0,0)
# obj_b=b(0,0)

# for i in (obj_a,obj_b):
#     i.input()
#     i.info()







class A():
     def __init__(self,name,father_Name):
        self.name=name
        self.father=father_Name
     def input(self):
        self.name=input("Enter your Name :")
        self.father=input("Enter your Father Name :")
     def info(self):
        print(self.name,self.father)


class b():
     def __init__(self,name,father_Name):
        self.name=name
        self.father=father_Name
     def input(self):
        self.name=input("Enter your Name :")
        self.father=input("Enter your Father Name :")
     def info(self):
        print(self.name,self.father)

def func(obj):
    obj.input()
    obj.info()


obj_a=A(0,0)
obj_b=b(0,0)

func(obj_a,obj_b)