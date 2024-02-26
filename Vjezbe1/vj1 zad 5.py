import matplotlib.pyplot as plt

def unesi_koordinate(tocka):
    while True:
        try:
            x = float(input(f"Unesite x koordinatu za točku {tocka}: "))
            y = float(input(f"Unesite y koordinatu za točku {tocka}: "))
            return x, y
        except ValueError:
            print("Pogrešan unos! Molimo unesite broj.")

def jednadzba_pravca(tocka1, tocka2, prikazi_graf=True, spremi_kao_pdf=False, naziv_pdf=None):
    x1, y1 = tocka1
    x2, y2 = tocka2

    if x1 == x2:
        jednadzba = f"Pravac je vertikalan i njegova jednadžba je x = {x1}"
    else:
        nagib = (y2 - y1) / (x2 - x1)
        odsjecak = y1 - nagib * x1
        jednadzba = f"Jednadžba pravca je y = {nagib} * x + {odsjecak}"

        # Grafički prikaz
        x_values = [x1, x2]
        y_values = [y1, y2]

        plt.plot(x_values, y_values, 'ro', label='Točke')
        plt.plot([x1, x2], [nagib * x1 + odsjecak, nagib * x2 + odsjecak], label='Pravac')

        plt.xlabel('X koordinata')
        plt.ylabel('Y koordinata')
        plt.title('Graf pravca koji prolazi kroz dvije točke')
        plt.legend()

        if prikazi_graf:
            plt.show()

        if spremi_kao_pdf:
            if naziv_pdf is None:
                naziv_pdf = input("Unesite ime PDF datoteke: ")
            plt.savefig(f"{naziv_pdf}.pdf")

        plt.clf()  # Očisti graf kako bi mogao prikazati više grafova unutar istog izvođenja

    print(jednadzba)

    return jednadzba

def main():
    print("Unesite koordinate za prvu točku:")
    tocka1 = unesi_koordinate("A")

    print("\nUnesite koordinate za drugu točku:")
    tocka2 = unesi_koordinate("B")

    print("\nIzračunavanje jednadžbe pravca:")
    rezultat = jednadzba_pravca(tocka1, tocka2, prikazi_graf=True, spremi_kao_pdf=False)

    # Print rezultata možete i ovdje
    # print(rezultat)

if __name__ == "__main__":
    main()
