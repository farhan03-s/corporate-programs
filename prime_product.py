m = int(input("ENTER M VALUE: "))
n = int(input("ENTER N VALUE: "))

if m > n:
    print(0)
else:
    product = 1
    found = False   # to check if any prime exists
    for i in range(m, n + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count == 2:   # prime condition
            product *= i
            found = True
    if found:
        print("PRODUCT: ", product)
    else:
        print("No primes found in the range")

