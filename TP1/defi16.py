liste = [8, 4, 6, 1, 5]
min = liste[0]
for i in range(len(liste)-1):
    if (min > liste[i+1]):
        min = liste[i+1]
print(min)