liste = []
liste2 = []
for i in range(22):
    if(i % 2 == 0):
        liste.append(i)
print(liste)

for i in range(len(liste)):
    if(liste[i] != 20):
        liste2.append(liste[i]*liste[i+1])

print(liste2)

