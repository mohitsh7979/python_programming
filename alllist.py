a=int(input())
x=[]

for i in range(0,a):
    count=input()
    count=count.split()
    if count[0]=="insert":
        x.insert(int(count[1]),int(count[2]))
    if count[0]=="print":
        print(x)
    if count[0]=="remove":
        x.remove(int(count[1]))
    if count[0]=="append":
        x.append(int(count[1]))
    if count[0]=="sort":
        x.sort()
    if count[0]=="pop":
        x.pop()
    if count[0]=="reverse":
        x.reverse()

