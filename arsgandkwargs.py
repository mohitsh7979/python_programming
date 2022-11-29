def myfunc(*args):
    return (args)

c=myfunc(10,20,30,40,50,60)

print(c)

def myfunc(**kwargs):
    return (kwargs['fruit'])

c=myfunc(fruit='apple',vegitable='patoto')

print(c)