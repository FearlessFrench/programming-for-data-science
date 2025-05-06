
a = True
b = False

def x(a, b):
    return ((a and not b) or (b and not a))

def y(a,b):
    return (a != b)

def z(a,b):
    return (a + b > 0)

def u(a,b):
    return ((not a) == b)


print(u(a,b))