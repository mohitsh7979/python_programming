# try:                                      try handle our print statement 
#     print(a)
# except NameError:                           except handle the our error
#     print('Variable length is not defined')

# try:
#     print(a)
# except:
#     print('Variable length is not defined')

# try:
#     print("Hello")

# except:
#     print("Something Went Wrong")

# else:
#     print("Nothing Went Wrong")



# try:
#     print("Hello")

# except:                     
#     print("Something Went Wrong")

# finally:
#     print("try and except will be executed")


# try:
#     print(x)

# except:
#     print("Something Went Wrong")

# finally:
#     print("try and except will be executed")


# try:
#     f=open("data.txt","w")
#     try:
#         f.write("loream 3546")
#     except:
#         print("you can not write in txt file")
#     finally:
#         f.close()
# except:
#     print("something went wrong")


# x=5

# if x>0:
#     # print("yes")
#     raise Exception("Sorry,the number is grater zero") 


x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
