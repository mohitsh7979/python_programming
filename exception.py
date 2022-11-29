

# def add(a,b):
#     try:
#      return (a+b)
#     except:
#        print('Hey you can not add string and integer')
#     finally:
#        print('i allwayes run')


# num1=10
# num2=input('Please enter a nummber :')

# c=add(num1,num2)
# print(c)


def ask_for_int():
   while True:
      try:
          int(input("Please enter a number :"))
      except:
         print("This is not a number !")
         continue
      else:
         print("Yes thanku")
         break
      finally:
         print("End of try/except/finally")
         print("I will alwayes run at the end !")

a=ask_for_int()
print(a)

     
 