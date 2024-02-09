#ex1.1
grams=int(input())
def ounce(a:int):
    b=grams* 28.3495231
    return b
print(ounce(grams))
 #ex1.2
F =int (input())
def C(F:int):
   tem= (5/9) * (F-32)
   return tem
print(C(F))
#ex1.3
numlegs=94
numheads=35
def solve(numheads, numlegs):
 rabbits=(numlegs/2)-numheads
 chiken = numheads-rabbits
 print(rabbits, " ", chiken)
solve(numheads,numlegs)
#ex1.4
def filter_prime(number):
    for i in number:
       if i>1:
          for j in range(2,i):
             if(i%j)==0:
                break
          else: 
             print(i)
          prime=[int (i) for i in input().split()]
          filter_prime(prime)
  #ex1.5
def String(List):
    return ''.join(List)
def permute(a, b, c):
    if b==c:
        print(String(a))
    else:
        for i in range(b, c):
            a[b], a[i]=a[i], a[b]
            permute(a, b+1, c)
            a[b], a[i]=a[i], a[b]
s=str(input())
n=len(s)
a=list(s)
permute(a, 0, n)
 #ex1.6
text=input()
def reverse(text):
    return ' '.join(text.split()[::-1])
result=reverse(text)
print(result)
#ex1.7
def has_33(nums):
    for i in range(len(nums)-1):
        if (nums[i]==3 and nums[i+1]==3):
            return True
    return False
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
#ex1.8
def spy_game(nums):
    for i in range(0,len(nums)):
        if nums[i]==0:
            for a in range(i+1,len(nums)):
                if nums[a]==0:
                    for y in range(a+1,len(nums)):
                        if nums[y]==7:
                            return True
                else:
                    return False
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
#ex1.9
def vol(pi, r):
    return 4/3*pi*r**3
r=int(input())
pi=3.14
v=vol(pi, r)
print(v)
#ex1.10
def uniq(num):
    for i in range(len(num)):
        a=num.count(num[i])
        if a==1:
            print(num[i])
u=[int(i) for i in input().split()]
uniq(u)
#ex1.11
def palindrome(s):
    t=s[::-1]
    if s==t:
        print("is a palindrome")
    else:
        print("is not a Palindrome")
v=str(input())
palindrome(v)
#ex1.12
def histogram( a ):
    for i in a:
        res=''
        t=i
        while(t>0):
            res+='*'
            t=t-1
        print(res)
b=[int(i) for i in input().split()]
histogram(b)
#ex1.13
import random
num = random.randint(1, 20)
def guess_game(guess):
 cnt =0
 while num > 0:
  cnt+=1
  if guess == num:
            print("Good job, " + a + "! You guessed my number in "+str(cnt)+" guesses!")
            break
 else:
            if guess < num:
                print("Your guess is too low.")
                print("Take a guess.")
                guess = int(input())
               
            elif guess > num:
                print("Your guess is too high.")
                print("Take a guess.")
                guess = int(input())
            print ('Hello! What is your name?')
a = input()
print('Well, '+a+', I am thinking of a number between 1 and 20.')
print ('Take a guess.')
guess = int(input())

guess_game(guess)
#1.14





   
   