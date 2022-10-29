# n = input()
j = input()
lst1=j.split()
lst1=lst1.sort()
count =int(1)
print(lst1)
for i in range(1,len(lst1)):
    if(lst1[i]==lst1[i-1]):
        count = count +1;
    else:
        print(count)
        count = 1
    
