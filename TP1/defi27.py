choix = int(input("Choissisez la taille du triangle "))
count = 1
count2 = choix
for i in range(choix):
    print(" "*count2+"*"*count+"!"+"*"*count)
    count += 1
    count2 -= 1
