m = int(input("ENTER M VALUE: "))
n = int(input("ENTER N VALUE: "))

if m > n:
    print(0)
else:
    total = 0
    for i in range(m, n + 1):
        fact = 1
        for j in range(1, i + 1):
            fact *= j
        total += fact

    print("SUM:", total)
