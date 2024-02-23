#ex1
import cmath
degr = int(input('Input degree: '))
rad = (cmath.pi / 180) * degr
print("Output radian: " + str(rad))
#ex2
h=int(input('Height: '))
a=int(input('Base, first value: '))
b=int(input('Base, second value: '))
s=((a+b)/2)*h
print('Expected Output: ',s)
#ex3
from math import tan, pi
n=float(input('Input number of sides: '))
s=float(input('Input the length of a side: '))
p=n*((s**2)/(4*tan(pi/n)))
print('The area of the polygon is: ', p)
#ex4
a=float(input('Length of base: '))
b=float(input('Height of parallelogram: '))
s=a*b
print('Expected Output:', s)