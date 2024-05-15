from random import randint

# Algorytm poszukiwania leadera:
# Table: 1 1 1 0 0
# Leader - 1

# Table2: 1 1 1 0 0 0
# Brak leadera

#Table = [2, 3, 1, 1, 1, 2, 1]
Table = [randint(0, 2) for _ in range(5)]
print(f"Table: {Table}")

def leader(Table):
    leader = Table[0]
    ilosc = 1
    for i in range(1, len(Table)):
        if ilosc == 0:
            leader = Table[i]
            ilosc = 1
        else:
            if Table[i] == leader:
                ilosc += 1
            else:
                ilosc -= 1

    if ilosc == 0:
        print("Brak leadera")
    else:
        ilosc_leaderow = 0
        for i in range(len(Table)):
            if Table[i] == leader:
                ilosc_leaderow += 1
        if ilosc_leaderow > len(Table) // 2:
            print(f"Leader: {leader}")
        else:
            print("Brak leadera")


leader(Table)
print("\n")

# Inna wersja, polegajaca na policzeniu wystapien liczb za pomoca innej tablicy, nastepnie sprawdzajac, czy ilosc najczesciej wystepujacego elementu jest wieksza od polowy ilosci wszystkich liczb
# Nwm czy sie przyda
def leader2(Table):
    pomoc = []
    for i in range(max(Table) + 1):
        pomoc.append(0)

    for i in range(len(Table)):
        pomoc[Table[i]] += 1
    print(f"Tablica pomocna: {pomoc}")

    if max(pomoc) > len(Table) / 2:
        leader = pomoc.index(max(pomoc))
        print(f"Leader: {leader}")
    else:
        print("Brak leadera")

leader2(Table)

