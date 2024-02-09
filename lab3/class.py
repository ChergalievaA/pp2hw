#ex3.1
from curses.textpad import rectangle


class Myclass:

    def getstring(self):
        self.s = input()
    def printstring(self):
        print(self.s.upper())

a = Myclass()
a.getstring()
a.printstring()
#ex3.2
class Shape(object):
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length=l
    def area(self):
        return self.length*self.length
n=int(input())
aSquare=Square(n)
print(aSquare.area())
#ex3.3
class Rectangle():
    def __init__(self, l, w):
        self.length=l
        self.width=w
    def area(self):
        return self.length*self.width
n=int(input())
m=int(input())
newRec=Rectangle(n, m)
print(newRec.area())
#ex3.4
class point(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        return(self.x,self.y)
    def move(self,x,y):
        self.x+=x
        self.y+=y
    def dist(self,pt):
        dx=pt.x-self.x
        dy=pt.y-self.y
        return(dx**2+dy**2)**0.5
#ex3.5
class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,newcome):
        def __init__ (self,newcome):
            self.newcome = newcome
        self.balance+=newcome

    def withdraw(self,outcome):
        def __init__(self,outcome):
            self.outcome = outcome
        if self.balance >= outcome:
            self.balance-=outcome
        else:
            self.balance = 0

    def show(self):
        print(self.balance)


a = Account("Salamat",1000)
a.deposit(100)
a.withdraw(1500)
a.show()
#ex3.6
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

numbers = [23, 45, 67, 89, 12, 34, 56, 73, 97, 101]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print( prime_numbers)

            