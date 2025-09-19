m = int(input("ENTER M VALUE: "))
n = int(input("ENTER N VALUE: "))

if m > n:
    print(-1)
else:
    x = 1
    for i in range(m, n + 1):
        x = x*i
    print("PRODUCT:", x)
