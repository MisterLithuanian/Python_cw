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
reversed