m = int(input("ENTER M VALUE: "))
n = int(input("ENTER N VALUE: "))

if m > n:
    print(0)
else:
    total_sum = 0
    for i in range(m, n + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count = count + 1
        if count == 2:   # prime numbers have exactly 2 divisors
            total_sum = total_sum + i
    print("SUM: ", total_sum)
