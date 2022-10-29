# m={ "0":"aman",
#     "1":"mohit",
#     "2":"rohit",
#     "3":"aman",


# }
# print(m["2"])
# print(len(m))
# print(m.get("2"))
# print(m.keys())
# print(m.values())
# m["4"]="colors"
# print(m.keys())
# print(m.items())
# print(m)
# m["3"]="motu"
# m.update({"2":"nanu"})
# m.pop("2")
# del m["3"]
# del m
# m.clear()
# for i in m:
#  print(m[i])

# Nested Dict

# m={
#     "mohit":{
#         "age":"19",
#         "course":"bca"
#     },
#     "rohit":{
#         "age":"19",
#         "course":"bteach"
#     },
#     "aman":{
#         "age":"20",
#         "course":"cs"
#     }

# }
# print(m)
# print(m.keys())
# print(m.values())
# print(m.items())
x=('mohit','rohit','aman')
y=('1','2','3')
c=dict.fromkeys(x,y)
print(c)