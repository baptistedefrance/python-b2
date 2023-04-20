for i in range(100, 300, 2):
    digits = [int(d) for d in str(i)]
    if digits[0] == digits[1] or digits[1] == digits[2] or digits[0] == digits[2]:
        if sum(digits) == 7:
            print(i)
