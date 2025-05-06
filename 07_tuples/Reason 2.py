def f(z):
    return 2*z

def g(z):
    z += 1
    return z/2

def h(z):
    if (z>3):
        return z + f(g(z))
    else:
        return g(z)

def code_tracing2(z):
    print(h(z-1))
    z *= 2
    return h(z)

print(code_tracing2(3))
