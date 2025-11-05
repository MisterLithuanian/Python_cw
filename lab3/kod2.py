for i in range(31):  
    if i % 3 != 0:  
        print(i)
    
while True:
    user_input = input("Podaj liczbę rzeczywistą lub wpisz 'stop', aby zakończyć: ")
    
    if user_input == "stop":
        print("Koniec")
        break
    
    try:
        x = float(user_input)
        print(f"x = {x}, x^3 = {x*x*x}")
    except ValueError:
        print("Podano niepoprawną wartość")

def miarka(dlugosc):
    miarka_1 = '|'
    for i in range(dlugosc):
        miarka_1 += '....|'

    miarka_2 = '0'
    for i in range(1, dlugosc + 1):
        miarka_2 += str(i).rjust(5)

    return miarka_1 + '\n' + miarka_2

print(miarka(12))

def prostokat(wiersze, kolumny):
    pozioma = '+---' * kolumny + '+\n'
    pionowa = '|   ' * kolumny + '|\n'
    
    rysunek = ''
    for i in range(wiersze):
        rysunek += pozioma
        rysunek += pionowa
    rysunek += pozioma  
    
    return rysunek

print(prostokat(2, 4))

A = [1, 2, 3, 4, 5, 5, 6]
B = [4, 5, 6, 7, 8, 8]
wspolne = list(set(A) & set(B))
wszystkie = list(set(A) | set(B))
print("a) Elementy wspólne:", wspolne)
print("b) Wszystkie elementy:", wszystkie)

seq = [[], [4], [1, 2], [3, 4], [5, 6, 7]]
suma = [sum(s) for s in seq]
print(suma)

def roman2int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,'D': 500, 'M': 1000}                
    total = 0
    poprzednik = 0
    for ch in reversed(s):  
        value = roman[ch]
        if value < poprzednik:
            total -= value
        else:
            total += value
        poprzednik = value
    return total
print(roman2int("IV"))     
print(roman2int("VI"))  