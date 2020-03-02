
age = int(input("Quel est votre age: "))
annee_per = 2020 - int(input("En quel annee avez vous obtenu votre permit : "))
nombr_acc = int(input("Combien d'accident avez vous deja subit : "))

tarif = "Aucun"


if age < 25:
    if annee_per < 2:
        tarif = "Desole nous ne pouvons rien faire pour vous !!!" if nombr_acc else "Tarif rouge"
        print(tarif, "\n")

elif (age < 25 and annee_per > 2) or (age > 25 and annee_per < 2):
        tarif =  "Tarif orange" if not nombr_acc else "Tarif rouge" if nombr_acc == 1 else "Demande refuse"
        print(tarif, "\n")

elif (age > 25) and (annee_per > 2):
    tarif = "Tarif vert" if not nombr_acc else  "Tarif orange" if nombr_acc == 1 else "Tarif rouge" if nombr_acc == 2 else "Demande refuse"
    print(tarif, "\n")

dico_promo = {"Tarif vert":"Tarif bleu",  "Tarif orange":"Tarif vert", "Tarif rouge": "Tarif orange"}

if "Tarif" in tarif:
    print("Vous avez le", tarif, "\n")
    demande = int(input("Depuis combien de temps etes vous chez nous ? "))
    tarif = dico_promo[tarif] if demande > 5 else tarif
    print("Vous avez finalement le", tarif)