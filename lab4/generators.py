#ex1
def gen(n,k=1):
    while k<=n:
        yield k**2
        k+=1
n=int(input())
a=gen(n)
for i in a:
 print(i)
#ex2
 a=int(input())
def even(a):
    for i in range(a+1):
        if (i%2==0):
            yield i
for i in even(a):
    print(i,end=',')
#ex3
a=int(input())
def gen(a):
    for i in range(a+1):
        if i%3==0 and i%4==0:
            yield i
for i in gen(a):
    print(i)
#ex4
a=int(input())
b=int(input())
def square(a,b):
    for n in range(a,b+1):
        yield n**2
for i in square(a,b):
    print(i)
#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
n =int(input())
for num in countdown(n):
    print(num,end=' ')