cond = int(input("entrer votre âge:"))
per = int(input("entrer la durée de votre permis:"))
acc = int(input("entrer le nombre accident:"))

if cond < 25 and per<2 and acc == 0:
    print("refuse d'assurer")
elif cond<25 and per>=25 and acc == 0:
    print("tarf rouge")
elif cond>25 and per>2 and acc == 0:
    print("tarif vert")
else:
    print("tarif orange")
