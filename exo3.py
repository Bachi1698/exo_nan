n=1
liste=[1/n]
a = float(input("entrez un nombre:"))
while sum (liste) < a:
    n = n+1
    liste.append(1/n)
print("le plus petit entier est:",n )
