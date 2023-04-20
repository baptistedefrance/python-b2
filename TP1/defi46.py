def compte_mots_2_lettres(seq):
    for i in range(len(seq)):
        if(seq[i] != seq[-1]):
         if(seq[i] == seq[i+1]):
             print("ok")

compte_mots_2_lettres("ACCTAGCCCTA")