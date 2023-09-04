class Fruit:
    #  def __init__(self,name,kg,price):
    #     self.fruit_name=name
    #     self.kg=kg
    #     self.price=price


    def __init__(self):
        self.fruit_name=input("Enter name fruit :")
        self.kg=input("Enter kg :")
        self.price=input("Enter price :")


    def getoutput(self):
        print("fruit name is {} and quantity is {}kg and price is {}".format(self.fruit_name,self.kg,self.price))

print("How many objects wants to create")
n=int(input())

for i in range(0,n):
    print("Enter your object name")
    object_name=input()
    object_name=Fruit()
    object_name.getoutput()


# apple=Fruit()
# banana=Fruit()
# apple.getoutput()
# banana.getoutput()

