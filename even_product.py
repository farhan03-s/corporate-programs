m = int(input("ENTER M VALUE: "))
n = int(input("ENTER N VALUE: "))

if m > n:
    print(0)
else:
    x = 1
    found = False 
    for i in range(m, n + 1):
        if i % 2== 0:
            x *= i
            found = True

    if found:
        print("PRODUCT:", x)
    else:
        print(0)  
