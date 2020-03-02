from math import *
p = 0.9
f= "p**x - (1/x)"
e= "p**(x+1) - (1/(x+1))"
x = 1
while eval(e) > eval(f):
    x = x+1
print("il atteint son max en :", x)    





#while (p**r)*log(p)+(1/r**2) != 0 and (2*log(p)*(p**r)-(2/r**3))>=0:
    #r = r+1
    
#print("la fonction attend son maximun en:",r)
