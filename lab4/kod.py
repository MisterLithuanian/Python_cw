#kopiuje kod z 3.5 i 3.6 bo wczesniej zrobilem funkcje 
#4.2
def miarka(dlugosc):
    miarka_1 = '|'
    for i in range(dlugosc):
        miarka_1 += '....|'

    miarka_2 = '0'
    for i in range(1, dlugosc + 1):
        miarka_2 += str(i).rjust(5)

    return miarka_1 + '\n' + miarka_2

def prostokat(wiersze, kolumny):
    pozioma = '+---' * kolumny + '+\n'
    pionowa = '|   ' * kolumny + '|\n'
    
    rysunek = ''
    for i in range(wiersze):
        rysunek += pozioma
        rysunek += pionowa
    rysunek += pozioma  
    
    return rysunek
#4.3
def factorial(n):
    if(n=='0'):
        return 0
    wynik=1
    for i in range (1, n+1):
        wynik=i*wynik
    return wynik

print(factorial(5))
#4.4
def fibonnaci(n):
    a=0
    b=1
    pom=0
    for i in range(n-1):
        pom=a+b 
        a=b
        b=pom
    return b
#4.5
def odwracanie_ite(L,left,right):
    while left<right:
        L[left], L[right] = L[right], L[left]
        left=+1
        right=-1
    return L

def odwracanie_rek(L,left,right):
    if left>=right:  
        return L
    L[left], L[right] = L[right], L[left]
    return odwracanie_rek(L,left+1,right-1)
    

L=[1,3,5,7,8,2]
print(odwracanie_ite(L,2,4))
L=[1,3,5,7,8,2]
print(odwracanie_rek(L,2,4))

#4.6 
def sum_seq(sequence):
    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total += sum_seq(item)     
        else:
            total += item              
    return total

P=[1,[2,3],[4,5,6]]
print(sum_seq(P))
#4.7
def flatten(sequence):
    flat = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            flat.extend(flatten(item))   
        else:
            flat.append(item)           
    return flat
