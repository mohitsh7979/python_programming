# def create_cubes(n):
#     result=[]
#     for x in range(n):
#         result.append(x**3)
#     print(result)
    
# create_cubes(10)




# def create_cubes(n):

#     for x in range(n):
#        yield x**3
   
    
# for i in create_cubes(10):
#     print(i)



# def fibo(n):
#     a=1
#     b=1

#     for i in range(n):
#         yield a
#         a,b=b,a+b

# for num in fibo(10):
#     print(num)



# def simple_gen():
#     for x in range(3):
#         yield x

# for num in simple_gen():
#     print(num)


# a='Mohit'
# a_itr=iter(a)
# print(next(a_itr))
# print(next(a_itr))
# print(next(a_itr))
# print(next(a_itr))
# print(next(a_itr))


# def gensuares(n):
#     for i in range(n):
#         yield i**2

# for x in gensuares(10):
#     print(x)


import random
random.randint(1,10)

def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low,high)


for num in rand_num(1,10,12):
    print(num)