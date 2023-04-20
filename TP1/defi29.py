import random
movement = [-1, 1]
start = 0
count = 0
while start != 5:
    res = random.choice(movement)
    if(res == -1):
        start -= 1
    else:
     start += 1
    count += 1
print(count)

