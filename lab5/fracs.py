#from fractions import gcd   # Py2
from math import gcd   # Py3

def add_frac(frac1, frac2): 
        wynik=[0,0]
        pom=frac1[1]*frac2[1]
        wynik[0]=frac1[0]*frac2[1]+frac2[0]*frac1[1]
        wynik[1]=pom
        return wynik

def sub_frac(frac1, frac2): 
        wynik=[0,0]
        pom=frac1[1]*frac2[1]
        wynik[0]=frac1[0]*frac2[1]-frac2[0]*frac1[1]
        wynik[1]=pom
        return wynik      

def mul_frac(frac1, frac2):        # frac1 * frac2
    wynik=[0,0]
    wynik[0]=frac1[0]*frac2[0]
    wynik[1]=frac1[1]*frac2[1]
    return wynik  

def div_frac(frac1, frac2):        # frac1 / frac2
    wynik=[0,0]
    wynik[0]=frac1[0]*frac2[1]
    wynik[1]=frac1[1]*frac2[0]
    return wynik 

def is_positive(frac):             # bool, czy dodatni
    if(frac[0]*frac[1]>=0):
          return True
    else: 
          return False
    
def is_zero(frac):                  # bool, typu [0, x]
    if(frac[0]==0): 
          return True
    else:
          return False
    
def cmp_frac(frac1, frac2):        # -1 | 0 | +1
    d = sub_frac(frac1, frac2)
    if is_zero(d): return 0
    if is_positive(d): return 1
    return -1

def frac2float(frac):
     return frac[0]/frac[1]

a=[2,3]
b=[1,3]
print(add_frac(a,b))
print(sub_frac(a,b))
print(mul_frac(a,b))
print(div_frac(a,b))
print(is_positive(a))
print(is_zero(b))
print(cmp_frac(a,b))
print(frac2float(a))