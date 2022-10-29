a=int(input())
b=int(a%10)
c=int(a/10)
d=int(c%10)
e=int(c/10)
x=int(e*e*e)
y=int(d*d*d)
z=int(b*b*b)
total=x+y+z
print(x+y+z)
if a==total:
    print("Armstrong no")

else:
    print("Not Armstrong no")