"""
Scrie o listă comprehensivă care generează o listă a literelor majuscule dintr-un anumit șir de caractere.
De exemplu, dacă șirul de caractere este "Salut Lume", lista comprehensivă ar trebui să producă ['S', 'L'].
"""
# Solution
propozitie = input("Va rog introduceti propozitia:\n")
lista_majuscule = list(char for char in propozitie if char.isupper())
print(lista_majuscule)
