#ex1.1
import datetime
x = datetime.datetime.now() - datetime.timedelta(days =5)
print("substract five days from current date:")
print(x)
#ex1.2
import datetime
x=datetime.datetime.now()
one_day=datetime.timedelta(days=1)
y=x-one_day
t=x+one_day
print(y)
print(x)
print(t)
#ex1.3
import datetime
x = datetime.datetime.now()
y = x.replace(microsecond=0)
print( y)
#ex1.4
import datetime
x=datetime.datetime.now()
t=datetime.datetime.now()+datetime.timedelta(days=1)
difference=t-x
difference_in_seconds=difference.total_seconds()
print(difference_in_seconds)
#ex1.5
def gen(n,k=1):
    while k<=n:
        yield k**2
        k+=1
n=int(input())
a=gen(n)
for i in a:
 print(i)