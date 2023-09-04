# def abc(a,b,c=0,d=0):
#     print(a+b+c+d)
# abc(1,2)
# abc(1,2,3)
# abc(1,2,3,4)


# class A:
#     a="OOPS"
#     print(a)

# o1=A()
# o1.a


class myclass:
    def __init__(self,a,b,c=0,d=0):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def print(self):
        print(self.a+self.b+self.c+self.d)

o1=myclass(1,2)
o1=myclass(1,2,3)
o1.print()


