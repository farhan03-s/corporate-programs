m = int(input("ENTER M VALUE: "))
n = int(input("ENTER N VALUE: "))

if m > n:
    print(0)
else:
    total = 0
    for i in range(m, n + 1):
        total += i * i * i
    print("SUM OF CUBES:", total)
