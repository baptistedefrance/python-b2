sequence = ["A", "C", "G", "T", "T", "A", "G", "C", "T", "A", "A", "C", "G"]
complement = []

for i in sequence:
    if i == "A":
        complement.append("T")
    elif i == "T":
        complement.append("A")
    elif i == "C":
        complement.append("G")
    elif i == "G":
        complement.append("C")
print(complement)
