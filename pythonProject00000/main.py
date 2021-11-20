import random

def pop(l):
    print(l.pop(0) )
    print(l)



def push(l,n):

    s.append(n)
    print(s)

s = [random.randint(0, 100) for i in range(random.randint(1, 100))]
num=int(input('Введите число:'))
print(s)
pop(s)
push(s,num)

