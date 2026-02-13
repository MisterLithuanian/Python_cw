Program projekt_final realizuje wizualizację problemu plecakowego wykorzystując do tego programowanie dynamiczne.

Wykorzystuje on:
- Python wersję 3.12.10
- bibliotekę pygame w wersji 2.6.1

Instrukcja:
- Otwórz terminal i urochom program za pomocą komendy python projekt_final.py
- Wyświetli się tablica wraz z opisanymi wartościami("w" to waga przedmiotu a "v" to wartość) i dwa przyciski LOSUJ oraz START
- Kliknij START jeśli chcesz uruchomić algorytm
- Kliknij LOSUJ jeśli chcesz wylosować nowe liczby

Opis Działania Algorytmu:
- Program rozwiązuje problem za pomocą wzoru na programowanie dynamiczne:
    Jeśli waga przedmiotu jest większa niż aktualna pojemność w, przepisujemy wartość z wiersza wyżej.
    W przeciwnym wypadku wybieramy maksimum z:
        Wartości bez bieżącego przedmiotu: dp[i−1][w]
        Wartości bieżącego przedmiotu + najlepszego upakowania pozostałej wagi: profit[i−1]+dp[i−1][w−weight[i−1]].