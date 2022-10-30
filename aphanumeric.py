a=input()
c=[]
for i in a:
    b=int(i)
    c.append(b)

for j in range(0,len(c)):
    if ord(c[i])>=97 and ord(c[i]) <=122 :
        print("True") 

    if ord(c[i])>=65 and ord(c[i]) <=90 :
        print("True")   

    if ord(c[i])>=48 and ord(c[i]) <=57 :
        print("True")  
    
    if ord(c[i])>=97 and ord(c[i]) <=122 and  ord(c[i])>=65 and ord(c[i]) <=90 and  ord(c[i])>=48 and ord(c[i]) <=57 :
        print("True") 


print(c)
# for i in range(0,len(a)):
#     print(a)