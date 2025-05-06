

def get_pi(n):
    if n == 1:
        return 4
    return 4 * (-1)**(n+1) * (1/(2*n-1)) + get_pi(n-1)
n = 6
print(get_pi(n))