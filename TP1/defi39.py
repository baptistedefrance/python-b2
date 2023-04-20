import random
def gen_distrib(start, fin, n):
    for i in range(n):
     print(random.uniform(start, fin))
gen_distrib(1,10,4)

def calc_stat(liste):
   print(min(liste))
   print(max(liste))
   print(sum(liste)/len(liste))

calc_stat([1.998,0.9876,2.89798])

import random
for i in range(20):
    random_list = [random.uniform(0, 100) for j in range(100)]
    print(f"Liste {i+1} :")
    print(f"\tMinimum : {min(random_list)}")
    print(f"\tMaximum : {max(random_list)}")
    print(f"\tMoyenne : {sum(random_list)/len(random_list)}")
