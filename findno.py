a=[655,899,226,236,25,63,46]

a.sort()
print(a)

for i in range((len(a)-1),0,-1):

    if i==len(a)-4:
     break
    print(a[i])