# f=open("data.txt","r")
# print(f.read())

# specific part print
# f=open("data.txt","r")
# print(f.read(8))


# readline function return a single line
# f=open("data.txt","r")
# print(f.readline())
# print(f.readline())

# f=open("data.txt","r")

# for i in f:

#  print(i)

# it is good habit to run close function 
# f=open("data.txt","r")
# print(f.read())
# f.close()

# append method add a new content in our file and it will be add end of the file
# f=open("data.txt","a")
# f.write("And it is very imporatnt topic")
# f.close()

# f=open("data.txt","r")
# print(f.read())
# f.close()

# w method overide the text on pervious text
# f=open("data.txt","w")
# f.write("And it is very imporatnt topic")
# f.close()

# f=open("data.txt","r")
# print(f.read())
# f.close()

#create new file

# f=open("file.txt","x")

# f=open("file.txt","w")
# f.write("With the help of x keywprd we create a new file and after then with the help of w method we are going to add some txt in our txt file")

# f=open("file.txt","a")
# f.write("with the help of a method we add the some new text in our txt file")

# f=open("file.txt","r")
# print(f.read())


# f=open("mohit.txt","x")
# using the remove method we can delete the our txt file 
import os

# os.remove("mohit.txt")

# f=open("rohit.txt","x")

if os.path.exists("rohit.txt"):
    os.remove("rohit.txt")
else:
    print("Your file does not exist")
