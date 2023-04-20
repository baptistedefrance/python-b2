def isprime(nb):
    res = True
    for i in range(2,nb):
        if(nb % i == 0):
            res = False
    print(res)
isprime(13)

for i in range(100):
    isprime(i)