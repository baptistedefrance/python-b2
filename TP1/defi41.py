import random
def ajoute_nb_alea(liste):
    liste2 = [-10, 10]
    liste3 = []
    for i in range(len(liste)):
        res = random.choice(liste2)
        liste3.append(liste[i]+res)
    print(liste3)
ajoute_nb_alea([1,2,3,4])