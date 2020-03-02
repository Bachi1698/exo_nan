# Exercice 1
def exercice1():
    while True:
        temperature = input("Entrez une température: ")
        if not temperature:
            break
        temperature = int(temperature)
        if temperature <= 0:
            print("\nGlace !!!")
        elif 0 < temperature < 100:
            print("\nLiquide !!!") 
        else:
            print("\nVapeur")