
# Exercice 2
def exercice2():
    while True:
        temperature = input("Entrez une température: ")
        if not temperature:
            break
        temperature = int(temperature)
        a = (temperature <= 0)
        b = (0 < temperature < 100)
        msg = "Glace !!!" if a else "Liquide !!!" if b else "Vapeur"
        print("\n", msg)

exercice2()