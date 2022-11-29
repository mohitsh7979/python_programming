example=[1,2,3,4,5,6,7,8,9]

from random import shuffle


def shuffle_example(example):
    shuffle(example)
    return example

a=shuffle_example(example)
print(a)

mylist=[' ','o',' ']
b=shuffle_example(mylist)
print(b)

def player_guess():
    guess=''
    while guess not  in['0','1','2']:
     guess=input('pick a number :0,1,2 : ')

    return int(guess)

a=player_guess()
print(a)