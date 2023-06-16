"""
Scrie un program care primește o listă de numere ca intrare. Programul ar trebui să calculeze produsul tuturor
numerelor din listă. Cu toate acestea, dacă produsul depășește 100, programul ar trebui să oprească calculul și să
afișeze un mesaj care indică că produsul este prea mare. Folosește o buclă while și instrucțiunea break pentru a
încheia bucla când este necesar.
"""
# solution
lista_numere = input("Introdu numere separate prin virgula:\n").split(",")
rezultat = 1 # Inmultirea cu 0 este 0.
i = 0
while i < len(lista_numere):
    rezultat *= int(lista_numere[i])
    if rezultat > 100:
        print("Rezultatul este prea mare!")
        break
    i += 1
else:
    print(f"Rezultatul este: {rezultat}")
    