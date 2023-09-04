a=[10,20,30,40,50]
b=len(a)
print(b)
for i in range(0,int(len(a)/2)):
    temp=a[i]
    a[i]=a[(b-i)-1]
    a[(b-i)-1]=temp

print(a)

max=0
min=100000000000000000000

for i in range(0,len(a)):
    if a[i]>max:
        max=a[i]

for i in range(0,len(a)):
    if a[i]<min:
        min=a[i]


print(max)
print(min)




