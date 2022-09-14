number= 13195

primeFactor = 1
i = 2

while i <= number:
    print(" primeFactor:  " + str(primeFactor))
    print(" i:  " + str(i))
    print(" number:  " + str(number))
    if number % i == 0:
        primeFactor = i
        number = number / i
        print("    primeFactor:  " + str(primeFactor))
        print("    number:  " + str(number))
    else:
        i = i + 1

print(primeFactor)