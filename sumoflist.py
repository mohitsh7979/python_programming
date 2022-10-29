# a=[1,2,3,4,5]
# counter=0
# for i in range(0,len(a)):
#     counter+=a[i]
#     print(a[i])
# print("Total=",counter)



def multi(list1):
    counter=1
    for i in range(0,len(list1)):
        counter*=list1[i]


    return counter
    

list1=[1,2,3,4,5]
print(multi(list1))