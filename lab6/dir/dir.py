#ex1
import os
#path='C:\Users\aauly\Desktop\labs_pp2\labspp2\lab6\dir'
dir, file, all = 0, 0, 0
put=os.getcwd()
print("DIR:")
for target in os.listdir('.'):
    if os.path.isdir(os.path.join(target)): 
        dir+=1  
        print(target)
print('FILE:')
for target in os.listdir('.'):
    if os.path.isfile(os.path.join(target)):
        file+=1
        print(target)

print("ALL:")
for target in os.listdir('.'):
    all+=1
    print(target)
    
print(dir)
print(file)
print(all)
#ex2
import os
print('Exist:', os.access(r'C:\Users\aauly\Desktop\labs_pp2\labspp2\lab6\dir\ayau.txt', os.F_OK))
print('Readable:', os.access(r'C:\Users\aauly\Desktop\labs_pp2\labspp2\lab6\dir\ayau.txt', os.R_OK))
print('Writable:', os.access(r'C:\Users\aauly\Desktop\labs_pp2\labspp2\lab6\dir\ayau.txt', os.W_OK))
print('Executable:', os.access(r'C:\Users\aauly\Desktop\labs_pp2\labspp2\lab6\dir\ayau.txt', os.X_OK))
#ex3
import os
path=r'C:\Users\aauly\Desktop\labs_pp2\labspp2\lab6\dir\ayau.txt'
print("Test a path exists or not:")
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDirectory name of the path:")
print(os.path.dirname(path))
#ex4
import os
a = open(r'C:\Users\aauly\Desktop\labs_pp2\labspp2\lab6\dir\ayau.txt')
b = a.read()
c = b.split('\n')
print(len(c))
#ex5
fruits=['apple', 'banana', 'pear']
with open('ayau.txt', "w") as myfile:
        for i in fruits:
                myfile.write("%s\n" % i)
drop=open('ayau.txt')
print(drop.read())
#ex6
import string, os
for letter in string.ascii_uppercase:
    f = open(letter + '.txt', 'x')
#ex7
with open('ayau.txt','r') as firstfile, open('ayau1.txt','a') as secondfile:
    for line in firstfile:  
        secondfile.write(line)
#ex8
import os 
path=r'C:\Users\aauly\Desktop\labs_pp2\labspp2\lab6\dir\ayau1.txt'
print(os.path.exists(path))
print(os.remove(path))