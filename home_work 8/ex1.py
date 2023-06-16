"""
Scrie un program care generează numere aleatorii între 1 și 10 folosind un buclă while. Programul ar trebui să
continue generarea de numere până când generează un număr mai mare decât 8. Odată ce numărul este mai mare decât 8,
programul ar trebui să încheie bucla folosind instrucțiunea break.
"""

# Solution
import random
while True:
    numar = random.randint(1, 10)
    print(numar)

    if numar > 8:
        break
