countA = 0
countR = 0
countW = 0
liste = ["A", "R", "A", "W", "W", "A", "W", "A", "R", "W", "W", "R", "A", "G"]
for i in liste:
    if i == "A":
        countA += 1
    if i == "R":
        countR += 1
    if i == "W":
        countW += 1
print(countA, countW, countR)

