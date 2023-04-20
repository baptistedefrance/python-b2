def test_composable(mot, seq):
    for i in range(len(mot)):
        for j in range(len(seq)):
            if (seq[j] == mot[i]):
                print(seq[j])
test_composable("python", "aophrtkny")




