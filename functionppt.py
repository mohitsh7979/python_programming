# id=1
# name="mohit"
# salary=3000
# print("id no is {} name is {} and salary is {}".format(id,name,salary))

# id=2
# name="Rohit"
# salary=5000
# print("id no is {} name is {} and salary is {}".format(id,name,salary))


def args(*args):
    a=args
    for i in a:
        print(i)
    # for i in args:
    #     print(args)

# args("Hello","My name is mohit ","and my salary is",10000)


# def nextargs(a,*args):
#     print("Through is a ",a)
#     for i in args:
#         print("Through is args ",i)

# nextargs("Hello","my name is mohit"1,"and my salary is ",10000)


# def abc(list):
#     print("with function",list)
#     print(type(list))

# my={1:"mohit","300.":1000}

# print("before func",my)
# abc(my)


def employee(id,name,salary):
    print(id,name,salary)

employee( 1000,name="mohit",salary=1)