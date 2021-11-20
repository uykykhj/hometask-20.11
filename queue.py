import random

def pop(l):
    print(l.pop(0) )
    s=l



def push(l):
    l=int(input())
    s.append(l)
    print(s)
s = [random.randint(0, 100) for i in range(random.randint(1, 100))]
print(s,'!')
pop(s)
push(s)
