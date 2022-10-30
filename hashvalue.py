a=input()
lst=[]
for i in a:
    count=input()
        
    # count.split()
    lst.append(count)
print(lst)
c=tuple(lst)
print(c)
print(str(abs(hash(c))))




