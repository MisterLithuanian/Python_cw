line = """bl bla bla bla bla
bla ballala bla bla bla."""

words = line.split()
count = len(words)
print(count)

word = "pyton"
result = "_".join(word)
print(result)

line2 = "bla bla bla bla bla"

words = line2.split()
first_letters = ''.join(w[0] for w in words)
last_letters = ''.join(w[-1] for w in words)

print("Pierwsze litery:", first_letters)
print("Ostatnie litery:", last_letters)

words = line.split()
longest = max(words, key=len)
print("Najdłuższy wyraz:", longest)
print("Długość:", len(longest))

Tab = [12123, 304215, 1423]
result = ''.join(str(x) for x in Tab)
print(result)

line3 = "bla blabla bla blabla GvR bla bla blaaaa"
new_line = line.replace("GvR", "Guido van Rossum")
print(new_line)

words = line.split()
print("Alfabetycznie:", sorted(words))
print("Według długości:", sorted(words, key=len))

n = 100242424140300
zera = str(n).count('0')
print(zera)

L = [5, 25, 132, 9]
result = ''.join(str(x).zfill(3) for x in L)
print(result)
