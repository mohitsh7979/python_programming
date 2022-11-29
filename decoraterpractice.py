# def A(name):
#     print('Hello World !')

#     def B():
#         return('yes Your name is {}'.format(name))

#     def C():
#         return('Your name is not {}'.format(name))
    
#     if name=='Mohit':
#         return B
#     else:
#         return C

# c=A(input('Enter a String :'))
# print(c())


# def A():
#     print('My age is 19')

# def B(my_func):
#     print('My name is Mohit')
#     print(my_func())

# B(A)


def A(mohit):
    def wrap():
     print('Hey')
     mohit()
     print('By')
    return wrap


@A
def B():
    print('I am ')

B()
