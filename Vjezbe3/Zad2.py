def izracunaj_sumu(N):
    rezultat = 0
    for i in range(N):
        rezultat += 1/3
    for i in range(N):
        rezultat -= 1/3
    rezultat -= 5
    return rezultat

# Ispis konačnog rezultata za različit broj iteracija
iteracije = [200, 2000, 20000]
for N in iteracije:
    rezultat = izracunaj_sumu(N)
    print(f"Za {N} iteracija, konačni rezultat je: {rezultat}")
