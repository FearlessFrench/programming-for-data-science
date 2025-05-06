

def decimal_to_binary(n):
    if n > 1:
        decimal_to_binary(n//2)
    print(n%2, end='')

n = 44
print(decimal_to_binary(n))


num = 4
def float_to_binary(num):
    for i in range(num):
        print(i) 