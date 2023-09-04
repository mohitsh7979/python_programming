# class Bill:

#     def __init__(self,itemname,price,quantity,distance):
#         self.itemname=itemname
#         self.price=price
#         self.quantity=quantity
#         self.distance=distance
        
#     def getInfo(self):
#         print(f'item name is {self.itemname}')
#         print(f'item price is {self.price}')
#         print(f'item quantity is{self.quantity}')
#         print(f'Total amount is{(self.price * self.quantity)+(self.distance*10)}')

#     def discount(self):
#         if(self.quantity >=5):
#             print(f'discounted amount is {(self.price * self.quantity)+(self.distance*10)-100}')

# b=Bill('pizza',200,10,5)
# b.getInfo()
# b.discount()



class Regex():

    def __init__(self , price):
        self.price = price 


    def getInfo(self):
        print(f" Total fees is = {self.price}") 
        print(f" your discount is {(self.price*10)/100}") 
        print(f" your total discounted fees is {self.price-(self.price*0.1)}")

a = Regex(2000) 
a.getInfo() 