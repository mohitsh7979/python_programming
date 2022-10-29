a=[1,2,3,4,5]
c=[]
b=len(a)
for i in range(0,b):
    if a[i]%2!=0:
        c.append(a[i])

print(c)
