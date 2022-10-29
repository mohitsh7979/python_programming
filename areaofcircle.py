# import math
# def areacircle():
#     r=float(input("Enter radious of circle "))
#     x=math.pi
#     return x*(pow(r,2))

# print(areacircle())

# r=float(input("Enter radious of circle :"))

# import math
# c=x*r*r
# print(c)

# a=[1,2,3,4,5]
# b=len(a)
# count=a[0]
# a[0]=a[b-1]
# a[b-1]=count
# print(a)

# a=[1,2,3,4,5]
# b=len(a)
# print(a)
# c=int(input("Enter first index"))
# d=int(input("Enter second index"))
# count=a[c-1]
# a[c-1]=a[d-1]
# a[d-1]=count
# print(a)


n=int(input())
print(type(n))
h=[]
for i in range(0,n):
    a=input()
    h.append(a)
print(h)
b=len(h)
print(h)
c=int(input("Enter first index"))
d=int(input("Enter second index"))
count=h[c-1]
h[c-1]=h[d-1]
h[d-1]=count
print("Your new list :",h)


