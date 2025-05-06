def f(x):
    print('f ', x)
    x += 1
    return (x*x)//10
    
def g(x):
    print('g ', x)
    x = (7*x)%5
    return f(x+3)    


x = 5
print((f(g(f(x)))) + x)