    # Divide
    x = int(n) # n = '4'
    y = list(map(str, range(2,x+1))) # ['2', '3', '4']
    segment = " "
    z = segment.join(y) # '2 3 4'
    m = '\n'
    result = (z+m)*x

    a = list(map(str, range(1,x+1))) # ['1', '2', '3', '4']
    b = m.join(a)
    
    return result


    x = int(n)
    y = list(map(str, range(1,x+1))) # ['1', '2', '3', '4']
    p = " " 
    m = '\n'
    z = p.join(y)      
    a = '1 '*1 + z[2:] # '1 2 3 4'
    b = '2 '*2 + z[4:] # '2 2 3 4'
    c = '3 '*3 + z[6:] # '3 3 3 4'
    d = '4 '*4 + z[8:] # '4 4 4 4'
    e = '5 '*5 + z[10:]
    f = '6 '*6 + z[12:]
    g = '7 '*7 + z[14:]

    result = a+m+b+m+c+m+d+m+e+m+f+m+g+m
    return result
