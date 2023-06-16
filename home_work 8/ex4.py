"""
Scrie un program care primește o listă de șiruri de caractere ca intrare. Programul ar trebui să afișeze fiecare șir
de caractere pe o linie separată. Cu toate acestea, dacă un șir de caractere începe cu litera 'A', programul ar
trebui să sara peste acel șir și să treacă la următorul folosind instrucțiunea continue.
"""
# Solution
lista_cuvinte = input("Introdu numere separate prin virgula:\n").split(", ")
for str in lista_cuvinte:
    if str[0].upper() == 'A':
        continue
    print(str)
# solution with while
i = 0
while i < len(lista_cuvinte):
    if lista_cuvinte[i][0].upper() == 'A':
        i += 1
        continue
    print(lista_cuvinte[i])
    i += 1
