def even_check(my_list):
    a=[]
    for i in my_list:
        if i%2==0:
            a.append(i)
        else:
            pass
    return a
       

  
    

c=even_check([1,2,6])
print(c)