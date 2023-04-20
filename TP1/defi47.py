file = open('note.txt', "r")
lines = file.readlines()
file.close()
liste = []
for line in lines:
    if(float(line) > 10.0):
     print(line.strip()+" admis")
     liste.append(float(line.strip()))
    else:
       print(line.strip()+" recalé (t nul)")
       liste.append(float(line.strip()))

print("moyenne :", sum(liste)/len(liste))
