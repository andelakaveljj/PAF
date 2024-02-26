def unesi_koordinate(tocka):
    while True:
        try:
            x = float(input(f"Unesite x koordinatu za točku {tocka}: "))
            y = float(input(f"Unesite y koordinatu za točku {tocka}: "))
            return x, y
        except ValueError:
            print("Pogrešan unos! Molimo unesite broj.")

def izracunaj_pravac(tocka1, tocka2):
    x1, y1 = tocka1
    x2, y2 = tocka2

    if x1 == x2:
        print(f"Pravac je vertikalan i njegova jednadžba je x = {x1}")
    else:
        nagib = (y2 - y1) / (x2 - x1)
        odsjecak = y1 - nagib * x1
        print(f"Jednadžba pravca je y = {nagib} * x + {odsjecak}")

def main():
    print("Unesite koordinate za prvu točku:")
    tocka1 = unesi_koordinate("A")

    print("\nUnesite koordinate za drugu točku:")
    tocka2 = unesi_koordinate("B")

    print("\nIzračunavanje jednadžbe pravca:")
    izracunaj_pravac(tocka1, tocka2)

if __name__ == "__main__":
    main()
