import math

def aritmeticka_sredina(lista):
    return sum(lista) / len(lista)

def standardna_devijacija(lista):
    mean = aritmeticka_sredina(lista)
    variance = sum((x - mean) ** 2 for x in lista) / len(lista)
    return math.sqrt(variance)

# Uzorak podataka (10 točaka)
tocke = [12, 15, 18, 22, 25, 28, 30, 35, 40, 45]

# Računanje aritmetičke sredine i standardne devijacije
sredina = aritmeticka_sredina(tocke)
devijacija = standardna_devijacija(tocke)

# Ispis rezultata
print("Aritmetička sredina:", sredina)
print("Standardna devijacija:", devijacija)
