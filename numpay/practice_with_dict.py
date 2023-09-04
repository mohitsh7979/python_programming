# a={
#     1:"mohit",
#     2:"rohit",
#     3:"mannu"
# }

# print(a[1])
# print(type(a[1]))

# for i in a:
#     print(type(i))
#     print(a[i])


# a={
#     1:[100,200,300,400],
#     2:[500,600,700,800],
#     3:[900,1000,1001,1002]
# }

# print(a)

# for i in a:
#     b=a[i]

#     for i in b:
#         print(i)

# a={
#     1:{"a":100,"b":200,"c":300},
#     2:[500,600,700,800],
#     3:[900,1000,1001,1002]
# }

# print(a[1]["b"])

# a=dict(name="mohit",roll_no=21,address="mohit")
# print(a)
# print(a["name"])
# print(a.keys())
# print(a.get("name"))
# print(a.keys())
# a["pin_code"]=302002
# print(a)
# print(a.values())
# a["address"]="jaipur"
# print(a)
# print(a.items())

# if "name" in a:
#     print("yes")

# print(a.update({"address":"jaipur"}))
# print(a)

# print(a.update({"pin_code":302002}))
# print(a)

# a.pop("name")
# print(a)

# del a["name"]
# print(a)

# del a
# print(a)

# a.popitem()
# print(a)

# a.clear()
# print(a)

# for i in a:
#     print(i)

# for i in a:
#     print(a[i])

# for i in a.values():
#     print(i)

# for i in a.keys():
#     print(i)

# for i,j in a.items():
#      print(i,j)

# b=a

# b["name"]="rohit"

# print(b) modiify
# print(a) modifiy

# b=a.copy()

# b["name"]="rohit"

# print(b)
# print(a)

# b=dict(a)
# b["name"]="rohit"
# print(b)
# print(a)

# a={
#     'childern 1':{
#         'name':'amit',
#         'age':10
#     },

#     'childern 2':{
#         'name':'anu',
#         'age':12
#     },

#     'childern 3':{
#         'name':'mohit',
#         'age':19
#     }
# }

# print(a.keys())
# print(a.values())
# print(a.items())

# for i in a:
#     print(i)

# for i in a:
#     print(a[i]['name'])

# for i in a.values():
#     print(i)

# for i ,j in a.items():
#     print(i,j)

# childern1={

#     'name':'amit',
#     'age':10

# }

# childern2={

#     'name':'anu',
#     'age':12

# }

# childern3={

#      'name':'mohit',
#      'age':19

# }

# a={
#     'child1':childern1,
#     'child2':childern2,
#     'child3':childern3
# }

# print(a)

# x=('a','b','c')
# y=1

# z=dict.fromkeys(x,y)
# print(z)

# input1=input()
# input2=input()

# a={

#     'a':input1,
#     'b':input2

# }

# print(a)

# input1=input()
# input2=input()
# a=input()
# b=input()

# a={

#     a:input1,
#     b:input2

# }

# print(a)

# a={}

# items=int(input("How many items you want add in your dict : "))

# print(items)

# for i in range(0,items):
#     print(i)
#     b=input("Enter Your key :")
#     c=input("Enter your value :")
#     a[b]=c

# print(a)







# Now practice with set

# a={1,2,3,4}
# a={'a','b','c','d'}
# print(len(a))
# print(a)
# print(type(a))

a=set(("apple","bana","papaya"))
b={'a','b','c'}
# print(a)

# print('apple' in a)

# print(a.add("anu"))
# print(a)

# a.update(b)
 
# print(a)

# a.remove("bana")
# print(a)

# a.discard("bana")
# print(a)

# a.pop()
# print(a)

# a.clear()
# print(a)

# del a
# print(a)

# c=a.union(b)
# print(c)

# a.update(b)

# print(a)


# Now tuples

# a=(1,2,3,4)
# print(len(a))
# print(a[1])
# print(type(a))

# b=(b,)
# print(type(b)) This is tuple beacause tuple conatine atleast 2 value if you set a value in a parenthesis so at the it not a tuple its a list 

# b=("mohit")
# print(b)
# print(type(b)) # not a tuple its a string

# b=tuple(("mohit","rohit","amit"))
# print(b)

a = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# print(a[0:7])

# print(a[0:7:2])

# print(a[2:6])

# print(a[:4]) # considered automatic starting value 0
 
# print(a[2:]) # takeing automatic last value

# print(a[-4:-1])

# if "apple" in a:
#     print("yes")

# b=list(a)

# b[1]="mohit"

# a=tuple(b)

# print(a)

# b=list(a)

# b.append("anu")

# a=tuple(b)

# print(a)

# b=("mohit","rohit")

# print(a+b)

# b=("mohit","rohit","vishesh")

# i,j,k=b

# print(i)
# print(j)
# print(k)

# i,j,*k=a

# print(i)
# print(j)
# print(k)

# i=0

# while i< len(a):
#     print(a[i])
#     i=i+1

# Now list 

a=list(("mohit","rohit","aman"))
b=[1,2,3,4]
# print(a)

# a[1]="mannu"

# a.append("mannu")

# a.insert(1,"mannu")

# print(a.index("rohit"))

# print(a)

# a.extend(b)
# print(a)

# a.remove("mohit")
# print(a)

# a.pop(2)
# print(a)

[print(i) for i in a]



