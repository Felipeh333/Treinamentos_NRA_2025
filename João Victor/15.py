def maior (*args):
    
    l = list(args)

    l.sort()

    p = len(l)-1

    return(l[p])

## exemplo

print(maior(1, 2, 3, 4, 5, 6))
