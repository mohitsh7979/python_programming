# def hello(name='Mohit'):
#     print('The hello () function has been executed !')

#     def greet():
#         return '\t This is the greet() func inside hello !'
    
#     def welcome():
#         return '\t Welcome inside the hello and greet function'
    

#     if name=='Mohit':
#         return greet
#     else:
#         return welcome
    
  

# a=hello('Mohit')
# print(a())


# def cool():
#     def super_cool():
#         return 'I am very cool'
#     return super_cool
# b=cool()
# print(b())


# def hello():
#     print('My name is mohit')

# def other_func(some_def_func):
#     print('Other codes run here !')
#     print(some_def_func())

# other_func(hello)


# def new_decorator(original_func):

#     def wrap_func():
#         print('Some extra code , before the original function')

#         original_func()

#         print('Some extra code , after the orignal function !')

#     return wrap_func

# def func_needs_decorators():
#     print('I want to be decorater')

# a=new_decorator(func_needs_decorators)
# a()





def new_decorator(original_func):

    def wrap_func():
        print('Some extra code , before the original function')

        original_func()

        print('Some extra code , after the orignal function !')

    return wrap_func

@new_decorator
def func_needs_decorators():
    print('I want to be decorater')

func_needs_decorators()
