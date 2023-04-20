liste = [8, 3, 12.5, 45, 25.5, 52, 1]
resultat = []

while liste:
    minimum = liste[0]  
    for x in liste:
        if x < minimum:
            minimum = x 
    resultat.append(minimum) 
    liste.remove(minimum)

print(resultat)
