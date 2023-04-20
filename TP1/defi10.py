import random
def seq_alea(nb):
    liste = ["A","T","G","C"]
    for i in range(nb):
        print(random.choice(liste))
seq_alea(15)