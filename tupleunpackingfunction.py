# stock_price=[("Apple",200),("Google",300),("Microsoft",400)]
# print(type(stock_price))
# for i in stock_price:
#     for j in range(len(i)):

#      print(i[0])


stock_price=[("Apple",200),("Google",300),("Microsoft",400)]
print(type(stock_price))
# for i,j in stock_price:
#     print(i)
 
def employee_check(work_hour):
    curent_max=0
    employee_of_monthe=''

    for i ,j in work_hour:
        curent_max=j
        employee_of_monthe=i
    else:
        pass

    return (curent_max,employee_of_monthe)

result=employee_check(stock_price)
hours,name=employee_check(stock_price)
print(name)
print(result)