def jednadzba_pravca(tocka1, tocka2):
    x1, y1 = tocka1
    x2, y2 = tocka2

    if x1 == x2:
        print(f"Pravac je vertikalan i njegova jednadžba je x = {x1}")
    else:
        nagib = (y2 - y1) / (x2 - x1)
        odsjecak = y1 - nagib * x1
        print(f"Jednadžba pravca je y = {nagib} * x + {odsjecak}")

# Primjer poziva funkcije
tocka1 = (1, 2)
tocka2 = (3, 4)

jednadzba_pravca(tocka1, tocka2)
