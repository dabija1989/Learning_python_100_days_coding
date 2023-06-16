"""
 Scrie o listă comprehensivă care generează o listă a primelor litere ale fiecărui cuvânt dintr-un anumit enunț.
 De exemplu, dacă enunțul este "Python este minunat", lista comprehensivă ar trebui să producă ['P', 'e', 'm'].
"""
# Solution
propozitie = input("Va rog introduceti propozitia:\n")
lista_majuscule = list(char[0] for char in propozitie.split())
print(lista_majuscule)
