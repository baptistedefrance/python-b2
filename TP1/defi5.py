def main():
    semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    print(semaine[0], semaine[1],semaine[2],semaine[3], semaine[4],semaine[5])
    print(semaine[-1], semaine[-2])
    print(semaine[6])
    print(semaine[0:5])
    rev = list(reversed(semaine))
    print(semaine[::-1])
    print(rev)
main()