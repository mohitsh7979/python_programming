class A:

    def __init__(self,name,father_name,mother_name):
        
        self.name=name
        self.father_name=father_name
        self.mother_name=mother_name

    def input(self):

        self.name=input("Enter Your name")
        self.father_name=input("Enter your father name")
        self.mother_name=input("Enter your mother name")

    def output(self):

        print(self.name,self.father_name,self.mother_name)

        
o1=A()

o1.input(0,0)
o1.output(0,0)