#ce programme permet de déterminer l'etat de leau

a=int(input("entrez la température de l'eau:"))
if a<= 0:
    print("l'eau est à l'etat de glace")

elif 0<a and a<= 100:
        print("l'eau est à l'etat de liquide")
else:
        print("l'eau est à l'etat de vapeur")

