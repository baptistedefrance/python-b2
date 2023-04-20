def isprime(nb):
    res = "prime"
    for i in range(2,nb):
        if(nb % i == 0):
            res = "not prime"
    print(res)
isprime(13)