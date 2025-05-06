def fx(m,n):
    total = 0
    for x in range(1,10,3):
        print("x =", x)
        total = total+x
    for y in range(1, 9+2):
        print("y =", y)
        total += y
    return total

print(fx(1,9))
