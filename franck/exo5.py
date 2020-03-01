age=int(input("entrez votre age:"))
permis=int(input("Depuis combien de temps avez vous votre permis?"))
accident=int(input("Combien d'accident avez vous déjà eu?"))

if age < 25 and permis <2:
    if accident ==0:
        demande=int(input("depuis combien de temps etes vous chez nous?"))
        if demande >= 5:
            print("vous changez de tarif , vous passez du rouge à l'orange")
        else:
            print("votre tarif est le rouge ")
    else:
        print("désolé , nous n'avons pas d'assurance pour vous ")
if (age < 25 and permis >=2) or (age >= 25 and permis < 2):
    if accident ==0:
        demande=int(input("depuis combien de temps etes vous chez nous?"))
        if demande >= 5:
            print("vous changez de tarif , vous passez du orange au vert")
        else:
            print("votre tarif est l'orange")
    elif accident==1:
        demande=int(input("depuis combien de temps etes vous chez nous?"))
        if demande >= 5:
            print("vous changez de tarif , vous passez du rouge à l'orange")
        else:
            print("votre tarif est le rouge ")
        
    else:
        print("désolé , nous n'avons pas d'assurance pour vous ")
        
if age >= 25 and permis >= 2 :
    if accident ==0:
        demande=int(input("depuis combien de temps etes vous chez nous?"))
        if demande >= 5:
            print("vous changez de tarif , vous passez du vert au bleu")
        else:
            print("votre tarif est vert")
    elif accident==1:
        demande=int(input("depuis combien de temps etes vous chez nous?"))
        if demande >= 5:
            print("vous changez de tarif , vous passez de l'orange au vert")
        else:
            print("votre tarif est l'orange ")
            
    elif accident==2:
        demande=int(input("depuis combien de temps etes vous chez nous?"))
        if demande >= 5:
            print("vous changez de tarif , vous passez du rouge à l'orange")
        else:
            print("votre tarif est le rouge")
        
    else:
        print("désolé , nous n'avons pas d'assurance pour vous ")
     
    