

def get_alphabet():
    chaine = ""
    for i in range(97, 123):
        chaine += chr(i)
    return(chaine)
get_alphabet()

def test_composable(mot):
    count = 0
    var = get_alphabet()
    for i in range(len(mot)):
        for j in range(len(var)):
            if (var[j] == mot[i]):
                #var = var[j:]
                count += 1
    print(count)
test_composable("Portez ce vieux whisky au juge blond qui fume")

def test2(mot):
    var = get_alphabet()
    for i in range(len(var)):
        for j in range(len(mot)):
            if (var[i] == mot[j]):
                var = var[i:]
    print(var)
test2("Portez ce vieux whisky au juge blond qui fume")