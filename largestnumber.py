a=[1,2,3,4,5,10]
max=a[0]

for i in a:
    if i>max:
        max=i

for j in a:
    if j>max and j!=max:
        max=i

print("max=",max)



# a=[1,2,3,4,5,10]
# min=a[0]

# for i in a:
#     if i < min:
#         min=i

# print("min=",min)